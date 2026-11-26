#!/usr/bin/env python3
"""Enrich the festivals and films already in the guide from Wikidata, Wikipedia and Wikimedia Commons.

    python3 tools/extractors/enrich/extract.py fetch <cache-dir>   # query the sources (slow, polite, resumable)
    python3 tools/extractors/enrich/extract.py build <cache-dir>   # write data/enrich/*.json
    python3 tools/extractors/enrich/extract.py run                 # both, with a fresh temporary cache
    python3 tools/extractors/enrich/extract.py test                # self-check of the matching rules

Writes only its own shard, data/enrich/:
  festivals.json  per world festival (Wikidata id): FIAPF accreditation, usual month, how often,
                  languages, a short description and a Wikipedia article in another language when English has none.
  about.json      opening sentences from that other-language Wikipedia article (CC BY-SA, linked from the festival).
  films.json      per film id: Wikidata id, runtime, genres, IMDb id, and a Commons poster or still
                  (copied to data/enrich/posters/) with its licence, for films that have no artwork.
Wikidata is CC0. Images come only from Wikimedia Commons and keep their own licence and credit.
Every cached reply is kept, so a rerun after a rate limit carries on where it stopped.
"""
import collections, hashlib, html, http.client, json, shutil, os, re, statistics, sys, time, unicodedata, urllib.error, urllib.parse, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
OUT = os.path.join(ROOT, 'data', 'enrich')
WORLD = os.path.join(ROOT, 'data', 'world-festivals')
UA = {'User-Agent': 'filmfest-guide-data/1.0 (open data project; github.com/omshivaprakash/filmfest-guide)'}
WDQS = 'https://query.wikidata.org/sparql'
GAP = float(os.environ.get('ENRICH_GAP', '2'))  # seconds between requests to one host
WDQS_GAP = float(os.environ.get('ENRICH_WDQS_GAP', GAP))  # the query service can ask for one query a minute
FILM_CLASSES = 'wd:Q11424 wd:Q24862 wd:Q93204 wd:Q202866 wd:Q506240 wd:Q17517379 wd:Q226730'
OTHER_WIKIS = ['fr', 'es', 'de', 'it', 'pt', 'ru', 'pl', 'nl', 'cs', 'sv', 'tr', 'fa', 'ar', 'ja', 'zh', 'ko', 'hi', 'ca', 'uk', 'hu', 'ro', 'el', 'fi', 'da', 'no', 'he', 'id', 'sr', 'hr', 'bg', 'sk', 'sl', 'et', 'lt', 'lv', 'eu', 'gl']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
last_call = collections.defaultdict(float)


def get(url, data=None, accept='application/json', tries=12):
    host = urllib.parse.urlsplit(url).netloc
    for attempt in range(tries):
        time.sleep(max(0, last_call[host] + (WDQS_GAP if host == 'query.wikidata.org' else GAP) - time.time()))
        last_call[host] = time.time()
        try:
            request = urllib.request.Request(url, data=data, headers={**UA, 'Accept': accept})
            return urllib.request.urlopen(request, timeout=180).read()
        except urllib.error.HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504):
                raise
            wait = int(error.headers.get('Retry-After') or 0) or 30 * (attempt + 1)
        except (urllib.error.URLError, TimeoutError, http.client.HTTPException, ConnectionError):
            wait = 30 * (attempt + 1)
        print(f'  waiting {wait}s for {host} (attempt {attempt + 1})', file=sys.stderr)
        time.sleep(min(wait, 300))
    raise RuntimeError(f'{host} kept refusing; rerun later, the cache keeps what was fetched')


def cached(cache, name, fetch):
    path = os.path.join(cache, name)
    if not os.path.exists(path):
        data = fetch()
        with open(path + '.part', 'w') as out:
            json.dump(data, out)
        os.replace(path + '.part', path)
    return json.load(open(path))


def sparql(query, tries=12):
    body = get(WDQS, urllib.parse.urlencode({'query': query}).encode(), 'application/sparql-results+json', tries)
    rows = json.loads(body)['results']['bindings']
    return [{**{k: v['value'] for k, v in row.items()}, **{k + '_lang': v['xml:lang'] for k, v in row.items() if 'xml:lang' in v}} for row in rows]


def split_sparql(template, items, render):
    """Run template over items; a query that times out (cut-off JSON or repeated refusals) is split in half."""
    try:
        return sparql(template % render(items), tries=3 if len(items) > 1 else 12)
    except (RuntimeError, ValueError):
        if len(items) == 1:
            print(f'  skipped {items[0]}: query keeps failing', file=sys.stderr)
            return []
        half = len(items) // 2
        return split_sparql(template, items[:half], render) + split_sparql(template, items[half:], render)


def wiki_api(lang, site, **params):
    url = f'https://{lang}.{site}.org/w/api.php?' + urllib.parse.urlencode({**params, 'format': 'json', 'formatversion': 2})
    return json.loads(get(url))


def qid(uri):
    return uri.rsplit('/', 1)[1]


def key(text):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', text.lower()))


def person(text):
    return ' '.join(sorted(key(part) for part in text.split()))  # name order differs between sources


def literal(text):
    return '"' + text.replace('\\', '\\\\').replace('"', '\\"') + '"'


def chunks(items, size):
    return [items[i:i + size] for i in range(0, len(items), size)]


# ---------- festivals ----------

FESTIVAL_FACTS = '''SELECT ?f ?k ?v ?u WHERE { VALUES ?f { %s }
  { ?f wdt:P407|wdt:P2936 ?x . ?x rdfs:label ?v . FILTER(LANG(?v) = "en") BIND("lang" AS ?k) }
  UNION { ?f p:P2257/psv:P2257 [ wikibase:quantityAmount ?v ; wikibase:quantityUnit ?u ] . BIND("every" AS ?k) }
  UNION { ?f wdt:P2922 ?x . ?x rdfs:label ?v . FILTER(LANG(?v) = "en") BIND("month" AS ?k) }
  UNION { ?e wdt:P179 ?f . ?e wdt:P580|wdt:P585 ?d . BIND(STR(?d) AS ?v) BIND("edition" AS ?k) }
  UNION { ?f schema:description ?v . BIND("desc" AS ?k) }
  UNION { ?a schema:about ?f ; schema:isPartOf ?site ; schema:name ?t . ?site wikibase:wikiGroup "wikipedia" .
          BIND(CONCAT(STR(?site), "|", ?t) AS ?v) BIND("wiki" AS ?k) }
}'''


def fetch_festivals(cache):
    world = json.load(open(os.path.join(WORLD, 'world-festivals.json')))['festivals']
    ids = sorted(record['id'] for record in world)
    for n, part in enumerate(chunks(ids, 200)):
        cached(cache, f'fest-{digest(part)}.json', lambda: split_sparql(FESTIVAL_FACTS, part, lambda ids: ' '.join('wd:' + i for i in ids)))
        print(f'festival facts {n + 1}/{-(-len(ids) // 200)}', file=sys.stderr)
    cached(cache, 'fiapf.json', lambda: wiki_api('en', 'wikipedia', action='parse', page='FIAPF', prop='wikitext', redirects=1))
    # Other-language opening sentences for festivals with no English article, 20 titles per request.
    facts = festival_facts(cache, world)
    wanted = collections.defaultdict(list)
    for q, fact in facts.items():
        if fact.get('wiki') and not fact['wiki'].startswith('https://en.'):
            lang = fact['wiki'].split('//')[1].split('.')[0]
            wanted[lang].append(urllib.parse.unquote(fact['wiki'].rsplit('/wiki/', 1)[1]).replace('_', ' '))
    for lang, titles in sorted(wanted.items()):
        for n, part in enumerate(chunks(sorted(set(titles)), 20)):
            cached(cache, f'about-{lang}-{n:03}.json', lambda: wiki_api(lang, 'wikipedia', action='query', prop='extracts', exintro=1, explaintext=1, exsentences=2, redirects=1, titles='|'.join(part)))
        print(f'about texts {lang}: {len(titles)}', file=sys.stderr)


def usual_month(dates):
    # shortcut: year-only dates come back as 1 January, so that day is ignored; a real 1 January opening is lost.
    months = collections.Counter(int(d[5:7]) for d in dates if re.match(r'\d{4}-\d\d', d) and d[4:10] != '-01-01')
    if sum(months.values()) < 2:
        return None
    month, count = months.most_common(1)[0]
    return MONTHS[month - 1] if count * 2 > sum(months.values()) else None  # a clear majority of editions


def frequency(amount, unit, dates):
    if amount and unit.endswith('/Q577'):  # unit: year
        return {1: 'Annual', 2: 'Biennial', 3: 'Triennial'}.get(round(float(amount)))
    if amount and unit.endswith('/Q5151'):  # unit: month
        return 'Twice a year' if round(float(amount)) == 6 else None
    years = sorted({int(d[:4]) for d in dates if re.match(r'\d{4}', d)})
    if len(years) >= 3:
        gap = statistics.median(b - a for a, b in zip(years, years[1:]))
        return {1: 'Annual', 2: 'Biennial'}.get(gap)
    return None


def pick_wiki(links):
    if not links:
        return None
    by_lang = {site.split('//')[1].split('.')[0]: (site, title) for site, title in links}
    for lang in ['en'] + OTHER_WIKIS:
        if lang in by_lang:
            site, title = by_lang[lang]
            return site + 'wiki/' + urllib.parse.quote(title.replace(' ', '_'))
    site, title = sorted(links)[0]
    return site + 'wiki/' + urllib.parse.quote(title.replace(' ', '_'))


def festival_facts(cache, world):
    rows = [row for name in sorted(os.listdir(cache)) if name.startswith('fest-') for row in json.load(open(os.path.join(cache, name)))]
    raw = collections.defaultdict(lambda: collections.defaultdict(list))
    for row in rows:
        raw[qid(row['f'])][row['k']].append((row.get('v'), row.get('u', '')))
    facts = {}
    for q, kinds in raw.items():
        dates = [v for v, _ in kinds['edition']]
        every = kinds['every'][0] if kinds['every'] else (None, '')
        fact = {
            'month': ([v for v, _ in kinds['month']] or [None])[0] or usual_month(dates),
            'every': frequency(every[0], every[1], dates),
            'langs': sorted({v for v, _ in kinds['lang']}) or None,
            'editions': len(dates) or None,
            'wiki': pick_wiki([tuple(v.split('|', 1)) for v, _ in kinds['wiki']]),
        }
        facts[q] = {k: v for k, v in fact.items() if v}
    return facts


def descriptions(cache):
    """English Wikidata description, else the first other-language one, by festival."""
    out = {}
    for name in sorted(os.listdir(cache)):
        if not name.startswith('fest-'):
            continue
        for row in json.load(open(os.path.join(cache, name))):
            if row['k'] == 'desc':
                out.setdefault(qid(row['f']), {})[row.get('v_lang', '')] = row['v']
    return out


def fiapf_accreditation(cache, world):
    """FIAPF accreditation by festival, from the accredited-festivals table on the English Wikipedia FIAPF article:
    'A-list' for festivals marked with an asterisk, otherwise 'Accredited'."""
    return fiapf_from_wikitext(json.load(open(os.path.join(cache, 'fiapf.json')))['parse']['wikitext'], world)


def fiapf_from_wikitext(text, world):
    text = re.split(r'==\s*Former accredited', text)[0]  # withdrawn festivals come after this heading
    at = text.find('Accredited film festivals')
    by_title = {urllib.parse.unquote(r['wiki'].rsplit('/wiki/', 1)[1]).replace('_', ' ').lower(): r['id'] for r in world if r.get('wiki')}
    by_name = {key(r['name']): r['id'] for r in world}
    found = {}
    for table in re.findall(r'\{\|.*?\n\|\}', text[at:] if at >= 0 else '', re.S):
        for row in table.split('\n|-')[1:]:
            cells = [cell.strip() for cell in row.split('\n|')[1:]]
            if len(cells) < 2:
                continue  # header rows use '!'
            link = re.search(r'\[\[([^\]|#]+)(?:\|([^\]]+))?\]\]', cells[1])  # the Festival column, not the city
            if link:
                q = by_title.get(link.group(1).strip().lower()) or by_name.get(key(link.group(2) or link.group(1)))
                if q:
                    found[q] = 'A-list' if '*' in cells[1] else 'Accredited'
    return found


def build_festivals(cache):
    world = json.load(open(os.path.join(WORLD, 'world-festivals.json')))['festivals']
    known = {r['id']: r for r in world}
    english_about = json.load(open(os.path.join(WORLD, 'world-about.json')))
    facts = festival_facts(cache, world)
    fiapf = fiapf_accreditation(cache, world)
    descs = descriptions(cache)
    about, shard = {}, {}
    extracts = {}
    for name in sorted(os.listdir(cache)):
        if name.startswith('about-'):
            lang = name.split('-')[1]
            for page in json.load(open(os.path.join(cache, name))).get('query', {}).get('pages', []):
                if page.get('extract'):
                    extracts[(lang, page['title'])] = page['extract'].strip()
            reply = json.load(open(os.path.join(cache, name))).get('query', {})
            for move in reply.get('redirects', []) + reply.get('normalized', []):
                if (lang, move['to']) in extracts:
                    extracts[(lang, move['from'])] = extracts[(lang, move['to'])]
    for q, record in known.items():
        fact = dict(facts.get(q, {}))
        if record.get('wiki') or (fact.get('wiki') or '').startswith('https://en.'):
            fact.pop('wiki', None)  # world-festivals.json already links the English article
        if q in fiapf:
            fact['fiapf'] = fiapf[q]
        if not record.get('desc') and descs.get(q):
            fact['desc'] = descs[q].get('en') or descs[q].get('mul') or next(iter(descs[q].values()))
        if fact.get('wiki') and q not in english_about:
            lang = fact['wiki'].split('//')[1].split('.')[0]
            title = urllib.parse.unquote(fact['wiki'].rsplit('/wiki/', 1)[1]).replace('_', ' ')
            if extracts.get((lang, title)):
                about[q] = {'lang': lang, 'text': extracts[(lang, title)]}
        if fact:
            shard[q] = fact
    return shard, about, fiapf


# ---------- films ----------

FILM_BY_TITLE = '''SELECT ?f ?l ?year WHERE { VALUES ?l { %s } VALUES ?c { %s }
  { ?f rdfs:label ?l } UNION { ?f skos:altLabel ?l }
  ?f wdt:P31 ?c . OPTIONAL { ?f wdt:P577 ?d . BIND(YEAR(?d) AS ?year) } }'''
FILM_FACTS = '''SELECT ?f ?k ?v ?u WHERE { VALUES ?f { %s }
  { ?f wdt:P57 ?x . ?x rdfs:label ?v . FILTER(LANG(?v) = "en") BIND("dir" AS ?k) }
  UNION { ?f wdt:P495 ?x . ?x rdfs:label ?v . FILTER(LANG(?v) = "en") BIND("country" AS ?k) }
  UNION { ?f wdt:P136 ?x . ?x rdfs:label ?v . FILTER(LANG(?v) = "en") BIND("genre" AS ?k) }
  UNION { ?f p:P2047/psv:P2047 [ wikibase:quantityAmount ?v ; wikibase:quantityUnit ?u ] . BIND("runtime" AS ?k) }
  UNION { ?f wdt:P3383 ?v . BIND("poster" AS ?k) }
  UNION { ?f wdt:P18 ?v . BIND("image" AS ?k) }
  UNION { ?f wdt:P345 ?v . BIND("imdb" AS ?k) }
}'''


def film_titles(films):
    titles = set()
    for film in films:
        titles.add(film['title'])
        titles.add(film['title'].title())
    return sorted(t for t in titles if t.strip())


def all_films():
    """catalog.json plus the extractor shards listed in data/shards.json, as the app loads them."""
    films = json.load(open(os.path.join(ROOT, 'catalog.json')))['films']
    for path in json.load(open(os.path.join(ROOT, 'data', 'shards.json'))):
        if os.path.exists(os.path.join(ROOT, path)):
            films += [{**film, '_from': path} for film in json.load(open(os.path.join(ROOT, path))).get('films', [])]
    return films


def digest(items):
    return hashlib.sha1('\n'.join(items).encode()).hexdigest()[:12]  # cache names follow the content, so a changed list refetches


def title_chunks(films):
    # shortcut: films carrying a Wikidata id skip title matching; the 21,000 unlinked world-editions films
    # are not title-matched yet (about 90 more queries), next batch.
    films = [f for f in films if not f.get('wikidata') and f.get('_from') != 'data/world-editions/catalog.json']
    return [(f'film-title-{digest(part)}.json', part) for part in chunks(film_titles(films), 250)]


def fact_chunks(candidates):
    return [(f'film-facts-{digest(part)}.json', part) for part in chunks(sorted(candidates), 300)]


def picture_files(cache, candidates):
    rows = [row for name, _ in fact_chunks(candidates) for row in json.load(open(os.path.join(cache, name)))]
    return sorted({urllib.parse.unquote(row['v'].rsplit('/', 1)[1]) for row in rows if row['k'] in ('poster', 'image')})


def fetch_films(cache):
    films = all_films()
    todo = title_chunks(films)
    for n, (name, part) in enumerate(todo):
        cached(cache, name, lambda: split_sparql(FILM_BY_TITLE, part, lambda titles: (' '.join(f'{literal(t)}@en {literal(t)}@mul' for t in titles), FILM_CLASSES)))
        print(f'film titles {n + 1}/{len(todo)}', file=sys.stderr)
    candidates = film_candidates(cache, films)[1]
    for n, (name, part) in enumerate(fact_chunks(candidates)):
        cached(cache, name, lambda: split_sparql(FILM_FACTS, part, lambda ids: ' '.join('wd:' + q for q in ids)))
        print(f'film facts {n + 1}', file=sys.stderr)
    files = picture_files(cache, candidates)
    for part in chunks(files, 50):
        # 330 px is one of the thumbnail widths Wikimedia serves; other widths are refused (HTTP 400).
        try:
            reply = cached(cache, f'commons-{digest(part)}.json', lambda: wiki_api('commons', 'wikimedia', action='query', prop='imageinfo', iiprop='url|extmetadata', iiurlwidth=330, iiextmetadatafilter='Artist|LicenseShortName|LicenseUrl', titles='|'.join('File:' + f for f in part)))
        except RuntimeError as error:
            print(f'  skipped {len(part)} Commons files: {error}', file=sys.stderr)
            continue
        # Images are copied into the repository, so the page makes no requests to outside services.
        for page in reply.get('query', {}).get('pages', []):
            url = (page.get('imageinfo') or [{}])[0].get('thumburl')
            path = os.path.join(cache, 'img', digest([page['title']]) + '.jpg')
            if url and not os.path.exists(path):
                os.makedirs(os.path.dirname(path), exist_ok=True)
                try:
                    image = get(url, accept='image/*', tries=3)
                except (RuntimeError, urllib.error.HTTPError) as error:  # one missing poster must not cost the whole run
                    print(f'  skipped image {page["title"]}: {error}', file=sys.stderr)
                    continue
                with open(path + '.part', 'wb') as out:
                    out.write(image)
                os.replace(path + '.part', path)
    print(f'film pictures {len(files)}', file=sys.stderr)


def film_candidates(cache, films):
    by_title, years = collections.defaultdict(set), collections.defaultdict(set)
    for name, _ in title_chunks(films):
        if os.path.exists(os.path.join(cache, name)):
            for row in json.load(open(os.path.join(cache, name))):
                by_title[key(row['l'])].add(qid(row['f']))
                if row.get('year'):
                    years[qid(row['f'])].add(int(row['year']))
    wanted = {q for film in films for q in by_title.get(key(film['title']), ()) if near(years[q], film['year'], 2)}
    wanted |= {film['wikidata'] for film in films if film.get('wikidata')}
    return (by_title, years), wanted


def near(years, year, gap):
    return any(abs(y - year) <= gap for y in years)


def match(film, candidates, years, directors, countries):
    """The Wikidata film for a catalogue film: same title, a year within two, and the same director
    (or, with no director on either side, the same country and a year within one)."""
    made_by = {person(name) for role, name in film['credits'] if 'direct' in role.lower()}
    made_in = {key(c) for c in (film.get('country') or '').split(', ') if c}
    hits = []
    for q in sorted(candidates):
        if not near(years[q], film['year'], 2):
            continue
        if made_by and directors[q]:
            ok = bool(made_by & directors[q])
        else:
            ok = bool(made_in & countries[q]) and near(years[q], film['year'], 1)
        if ok:
            hits.append(q)
    return hits[0] if len(hits) == 1 else None  # two equally good matches: leave it unlinked


def minutes(amount, unit):
    value = float(amount)
    if unit.endswith('/Q11574'):
        value /= 60
    elif unit.endswith('/Q25235'):
        value *= 60
    elif not unit.endswith('/Q7727'):
        return None
    return round(value) if 0 < value < 1000 else None


def credit_line(meta):
    artist = re.sub(r'<[^>]+>', '', html.unescape(meta.get('Artist', {}).get('value', ''))).strip()
    return re.sub(r'\s+', ' ', artist)[:120] or 'Wikimedia Commons'


def build_films(cache):
    films = all_films()
    (by_title, years), candidates = film_candidates(cache, films)
    facts = collections.defaultdict(lambda: collections.defaultdict(list))
    for row in (row for name, _ in fact_chunks(candidates) for row in json.load(open(os.path.join(cache, name)))):
        facts[qid(row['f'])][row['k']].append((row['v'], row.get('u', '')))
    directors = {q: {person(v) for v, _ in f['dir']} for q, f in facts.items()}
    countries = {q: {key(v) for v, _ in f['country']} for q, f in facts.items()}
    directors, countries = collections.defaultdict(set, directors), collections.defaultdict(set, countries)
    images = {}
    for part in chunks(picture_files(cache, candidates), 50):
            path = os.path.join(cache, f'commons-{digest(part)}.json')
            for page in (json.load(open(path)) if os.path.exists(path) else {}).get('query', {}).get('pages', []):
                info = (page.get('imageinfo') or [{}])[0]
                meta = info.get('extmetadata', {})
                local = os.path.join(cache, 'img', digest([page['title']]) + '.jpg')
                if os.path.exists(local) and meta.get('LicenseShortName'):
                    images[page['title'][5:]] = {
                        'local': local, 'source': info['descriptionurl'],
                        'credit': f"{credit_line(meta)}, {meta['LicenseShortName']['value']}, via Wikimedia Commons",
                        'license': meta['LicenseShortName']['value'], 'licenseUrl': meta.get('LicenseUrl', {}).get('value')}
    shard = {}
    shutil.rmtree(os.path.join(OUT, 'posters'), ignore_errors=True)
    for film in films:
        q = film.get('wikidata') or match(film, by_title.get(key(film['title']), ()), years, directors, countries)
        if not q or q not in facts:
            continue
        f = facts[q]
        entry = {'wikidata': q}
        runtimes = [m for m in (minutes(v, u) for v, u in f['runtime']) if m]
        if runtimes:
            entry['minutes'] = max(set(runtimes), key=runtimes.count)
        if f['genre']:
            entry['genres'] = sorted({v for v, _ in f['genre']} - {'drama film'} or {'drama film'})[:4]
        if f['imdb']:
            entry['imdb'] = f['imdb'][0][0]
        for kind in ('poster', 'image'):
            for v, _ in f[kind]:
                picture = images.get(urllib.parse.unquote(v.rsplit('/', 1)[1]).replace('_', ' '))
                if picture and 'poster' not in entry and not film.get('artwork'):
                    file = f"data/enrich/posters/{re.sub(r'[^A-Za-z0-9_-]', '_', film['id'])}.jpg"
                    os.makedirs(os.path.join(OUT, 'posters'), exist_ok=True)
                    shutil.copyfile(picture['local'], os.path.join(ROOT, file))
                    entry['poster'] = {k: v for k, v in picture.items() if k != 'local'} | {'file': file, 'kind': kind}
        if len(entry) > 1:
            shard[film['id']] = entry
    return shard


def write(name, data):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), 'w') as out:
        json.dump(data, out, ensure_ascii=False, separators=(',', ':'), sort_keys=True)
        out.write('\n')


def build(cache):
    festivals, about, fiapf = build_festivals(cache)
    films = build_films(cache)
    note = 'Wikidata (CC0), Wikipedia (CC BY-SA 4.0, linked per festival) and Wikimedia Commons (licence per image)'
    write('festivals.json', {'source': note, 'count': len(festivals), 'festivals': festivals})
    write('about.json', {'source': 'Wikipedia (CC BY-SA 4.0), linked per festival', 'count': len(about), 'festivals': about})
    write('films.json', {'source': note, 'count': len(films), 'films': films})
    count = lambda field: sum(1 for f in festivals.values() if field in f)
    print(f"festivals enriched {len(festivals)}: fiapf {len(fiapf)}, month {count('month')}, every {count('every')}, "
          f"langs {count('langs')}, desc {count('desc')}, other-language wiki {count('wiki')}, about {len(about)}")
    print(f"films enriched {len(films)}: runtime {sum('minutes' in f for f in films.values())}, genres {sum('genres' in f for f in films.values())}, "
          f"imdb {sum('imdb' in f for f in films.values())}, poster {sum('poster' in f for f in films.values())}")


def test():
    assert usual_month(['2020-02-10T00:00:00Z', '2021-02-11T00:00:00Z', '2022-03-01T00:00:00Z']) == 'February'
    assert usual_month(['2020-02-10T00:00:00Z', '2021-05-11T00:00:00Z']) is None
    assert usual_month(['2020-01-01T00:00:00Z', '2021-01-01T00:00:00Z']) is None
    assert frequency('1', 'http://www.wikidata.org/entity/Q577', []) == 'Annual'
    assert frequency(None, '', ['2001', '2003', '2005', '2007']) == 'Biennial'
    assert minutes('5400', 'http://www.wikidata.org/entity/Q11574') == 90
    assert minutes('90', 'http://www.wikidata.org/entity/Q7727') == 90
    film = {'title': 'X', 'year': 2020, 'credits': [['Director', 'Ana Lee']], 'country': 'India'}
    years = collections.defaultdict(set, {'Q1': {2019}, 'Q2': {2020}})
    directors = collections.defaultdict(set, {'Q1': {person('Lee Ana')}, 'Q2': {person('Bob')}})
    assert match(film, {'Q1', 'Q2'}, years, directors, collections.defaultdict(set)) == 'Q1'
    sample = ('==Accredited film festivals==\n{| class="wikitable"\n|-\n! Location\n! Festival\n|-\n| {{flagicon|FRA}} [[Cannes]]\n'
              "| '''[[Cannes Film Festival|Festival de Cannes]]*'''\n| Competitive\n|-\n| [[Kyiv]]\n| [[Molodist]]\n| Competitive\n|}\n"
              '== Former accredited film festivals ==\n{|\n|-\n| [[Adelaide]]\n| [[Adelaide Film Festival]]\n|}')
    world = [{'id': 'Q1', 'name': 'Cannes Film Festival', 'wiki': 'https://en.wikipedia.org/wiki/Cannes_Film_Festival'},
             {'id': 'Q2', 'name': 'Molodist'}, {'id': 'Q3', 'name': 'Adelaide Film Festival'}, {'id': 'Q4', 'name': 'Cannes'}]
    assert fiapf_from_wikitext(sample, world) == {'Q1': 'A-list', 'Q2': 'Accredited'}
    calls = []
    def fake(query, tries=12):
        calls.append(query)
        if query.count('wd:') > 1:
            raise ValueError('cut off')
        return [query]
    global sparql
    real, sparql = sparql, fake
    assert split_sparql('%s', ['A', 'B', 'C'], lambda ids: ' '.join('wd:' + i for i in ids)) == ['wd:A', 'wd:B', 'wd:C']
    sparql = real
    print('ok')


if __name__ == '__main__':
    command = sys.argv[1] if len(sys.argv) > 1 else ''
    if command == 'test':
        test()
    elif command == 'run':  # what the scheduled workflow calls: a fresh fetch, then build
        import tempfile
        cache = tempfile.mkdtemp(prefix='enrich-')
        fetch_festivals(cache)
        fetch_films(cache)
        build(cache)
    elif command in ('fetch', 'build') and len(sys.argv) == 3:
        os.makedirs(sys.argv[2], exist_ok=True)
        if command == 'fetch':
            fetch_festivals(sys.argv[2])
            fetch_films(sys.argv[2])
        else:
            build(sys.argv[2])
    else:
        sys.exit(__doc__)
