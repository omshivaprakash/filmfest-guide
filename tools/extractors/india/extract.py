"""Indian film festivals extractor: writes data/india/catalog.json (a shard in catalog.json shape).

    python3 tools/extractors/india/extract.py                    # fetch into .cache/india, then build
    python3 tools/extractors/india/extract.py fetch <cache-dir>   # Wikipedia + Wikidata, slow and polite
    python3 tools/extractors/india/extract.py build <cache-dir>   # parse the cache, write the shard
    python3 tools/extractors/india/extract.py test                # self-check of the cell parser

Sources: the English Wikipedia article of each festival (award tables and "YEAR: Title - Director"
lists, jury tables) and Wikidata (edition items, plus language, country, director and a one-line
description for every film the article links). Only facts are kept: titles, names, years and award
names. Every record links the Wikipedia revision it came from. Wikidata is CC0; Wikipedia is CC BY-SA.
Festivals with nothing extractable are left out and stay on the work-in-progress list.
"""
import json, os, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'data' / 'india' / 'catalog.json'
UA = {'User-Agent': 'filmfest-guide-data/1.0 (open data project; github.com/omshivaprakash/filmfest-guide)'}

# id matches the hand-listed worldFestivals entry (if any) and wikidata the world-festivals.json row, so the loader can drop both.
FESTIVALS = [
    dict(id='kiff', wikidata='Q474265', wiki='Kolkata International Film Festival', short='KIFF', region='West Bengal', lat=22.57, lon=88.36, url='https://www.kiff.in', description='Golden Royal Bengal Tiger, Indian languages and Bengali Panorama.'),
    dict(id='mami', wikidata='Q17075409', wiki='Mumbai Film Festival', name='MAMI Mumbai Film Festival', short='MAMI', region='Maharashtra', lat=19.08, lon=72.88, url='https://www.mumbaifilmfestival.com', description='South Asia competition and world cinema in Mumbai.'),
    dict(id='ciff-chennai', wikidata='Q5091441', wiki='Chennai International Film Festival', short='CIFF', region='Tamil Nadu', lat=13.08, lon=80.27, url='https://chennaifilmfest.com', description='Tamil and Indian Panorama competitions with world cinema.'),
    dict(id='piff', wikidata='Q7260105', wiki='Pune International Film Festival', short='PIFF', region='Maharashtra', lat=18.52, lon=73.86, url='https://www.piffindia.com', description='World and Marathi competitions in Pune.'),
    dict(id='miff', wikidata='Q1952566', wiki='Mumbai International Film Festival', name='Mumbai International Film Festival (documentary, short and animation)', short='MIFF', region='Maharashtra', lat=18.97, lon=72.82, url='https://miff.in', format='Documentary', description='Golden and Silver Conch for documentary, short fiction and animation.'),
    dict(id='kashish', wikidata='Q6935315', wiki='Mumbai Queer Film Festival', name='KASHISH Pride Film Festival', short='KASHISH', region='Maharashtra', lat=19.11, lon=72.86, url='https://mumbaiqueerfest.com', description='LGBTQ+ films from India and around the world.'),
    dict(id='diff', wikidata='Q5269134', wiki='Dharamshala International Film Festival', short='DIFF', region='Himachal Pradesh', lat=32.22, lon=76.32, url='https://diff.co.in', description='Independent cinema in the Himalayas.'),
    dict(id='jiff', wikidata='Q5860975', wiki='Jaipur International Film Festival', short='JIFF', region='Rajasthan', lat=26.91, lon=75.79, url='https://www.jiffindia.org', description='Features, shorts and documentaries in Jaipur.'),
    dict(id='jagran', wikidata='Q28173088', wiki='Jagran Film Festival', short='JFF', region='Delhi', lat=28.61, lon=77.21, url='https://www.jagranfilmfestival.com', description='A touring festival across Indian cities.'),
    dict(id='giff', wikidata='Q47086772', wiki='Guwahati International Film Festival', short='GIFF', region='Assam', lat=26.18, lon=91.75, url='https://giff.assam.gov.in', description='Assamese competition and world cinema in Guwahati.'),
    dict(id='icffi', wikidata='Q24904890', wiki="International Children's Film Festival India", short='ICFFI', region='Telangana', lat=17.36, lon=78.47, url='https://cfsindia.org', description='Films for children, the Golden Elephant.'),
    dict(id='osians', wikidata='Q634317', wiki="Osian's Cinefan Festival of Asian and Arab Cinema", short='Cinefan', region='Delhi', lat=28.61, lon=77.21, description='Asian and Arab cinema in New Delhi.'),
]
YEAR = re.compile(r'\b(19[5-9]\d|20[0-4]\d)\b')
ORDINAL = re.compile(r'\b(\d{1,2}(?:st|nd|rd|th))\b')


def get(url, data=None, tries=6):
    for attempt in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, data=data, headers={**UA, 'Accept': 'application/json, application/sparql-results+json'}), timeout=90).read()
        except Exception as error:  # 429 from Wikimedia: back off and retry
            print('retry', url[:90], error, file=sys.stderr)
            time.sleep(20 * (attempt + 1))
    raise RuntimeError(f'gave up on {url[:90]}')


def sparql(query):
    return json.loads(get('https://query.wikidata.org/sparql', urllib.parse.urlencode({'query': query}).encode()))['results']['bindings']


def val(binding, key):
    return binding.get(key, {}).get('value', '').replace('http://www.wikidata.org/entity/', '')


def fetch(cache):
    cache = Path(cache)
    (cache / 'wiki').mkdir(parents=True, exist_ok=True)
    for fest in FESTIVALS:
        path = cache / 'wiki' / f"{fest['id']}.json"
        if path.exists():
            continue
        title = urllib.parse.quote(fest['wiki'])
        body = json.loads(get(f'https://en.wikipedia.org/w/api.php?action=parse&format=json&prop=text|revid&redirects=1&maxlag=5&page={title}'))
        if 'parse' not in body:
            print('no article', fest['wiki'], file=sys.stderr)
            continue
        path.write_text(json.dumps({'title': body['parse']['title'], 'revid': body['parse']['revid'], 'html': body['parse']['text']['*']}))
        time.sleep(5)
    qids = ' '.join('wd:' + fest['wikidata'] for fest in FESTIVALS)
    editions = sparql(f'''SELECT ?f ?ed ?edLabel ?n ?start ?date WHERE {{ VALUES ?f {{ {qids} }} ?ed wdt:P179|wdt:P361 ?f .
      OPTIONAL {{ ?ed wdt:P393 ?n }} OPTIONAL {{ ?ed wdt:P580 ?start }} OPTIONAL {{ ?ed wdt:P585 ?date }}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }} }}''')
    (cache / 'editions.json').write_text(json.dumps(editions))
    titles = sorted({link for fest in FESTIVALS for link in links(cache, fest)})
    films = []
    for i in range(0, len(titles), 150):
        values = ' '.join(json.dumps(t, ensure_ascii=False) + '@en' for t in titles[i:i + 150])
        films += sparql(f'''SELECT ?t ?film ?desc ?kind ?langLabel ?countryLabel ?dirLabel ?date WHERE {{ VALUES ?t {{ {values} }}
          ?a schema:about ?film ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?t .
          ?film wdt:P31 ?kind . FILTER(?kind IN (wd:Q11424, wd:Q24862, wd:Q93204, wd:Q202866, wd:Q506240, wd:Q17517379))
          OPTIONAL {{ ?film schema:description ?desc FILTER(LANG(?desc) = "en") }}
          OPTIONAL {{ ?film wdt:P364 ?lang }} OPTIONAL {{ ?film wdt:P495 ?country }} OPTIONAL {{ ?film wdt:P57 ?dir }} OPTIONAL {{ ?film wdt:P577 ?date }}
          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }} }}''')
        time.sleep(2)
    (cache / 'films.json').write_text(json.dumps(films))


def links(cache, fest):
    import lxml.html
    path = Path(cache) / 'wiki' / f"{fest['id']}.json"
    if not path.exists():
        return []
    doc = lxml.html.fromstring(json.loads(path.read_text())['html'])
    return [a.get('title') for a in doc.xpath('//table[contains(@class,"wikitable")]//a[@title] | //li//i//a[@title]') if not a.get('href', '').startswith('#')]


def clean(text):
    text = re.sub(r'\[(?:\d+|[a-z]|citation needed|note \d+)\]', '', text)
    return re.sub(r'\s+', ' ', text).strip(' ,;:-–|')


def text_of(node):
    for block in node.iter('p', 'br', 'li', 'div'):  # block breaks become spaces; inline tags join as written
        block.text, block.tail = ' ' + (block.text or ''), ' ' + (block.tail or '')
    return clean(node.text_content())


def strip_refs(node):
    for bad in node.xpath('.//sup|.//style|.//span[contains(@class,"sortkey")]'):
        bad.drop_tree()
    return node


def parse_cell(node):
    """One winner cell -> (title, person, director, wiki title of the film link), any can be ''. Kept as plain strings."""
    strip_refs(node)
    text = text_of(node)
    if not text or text.lower() in {'—', '-', 'n/a', 'not awarded', 'no award'}:
        return None
    italics = [text_of(i) for i in node.xpath('.//i') if text_of(i)]
    italic = italics[0] if italics else ''
    link = next((a.get('title') for a in node.xpath('.//i//a[@title]|.//a[@title][.//i]')), '')
    person = director = ''
    if len(italics) > 1 and re.match(r'^for\b', clean(text.partition(italics[0])[2])):
        return italics[1], italics[0], '', link  # "<i>Person</i> for <i>Film</i>"
    if italic:
        before, _, after = text.partition(italic)
        before, after = clean(before), clean(after)
        if re.search(r'\bfor$', before):
            person = clean(before[:-3])
        after = re.sub(r'^\(|\)$', '', after).strip()
        after = clean(re.sub(r'^(?:directed by|dir\.|by)\b', '', after, flags=re.I))
        if after and not person:
            director = clean(after.split('|')[0])
        title = italic
    elif ' for ' in text:
        person, title = (clean(part) for part in text.split(' for ', 1))
        link = next((a.get('title') for a in node.xpath('.//a[@title]') if text_of(a) == title), '')
    elif ' by ' in text:
        title, director = (clean(part) for part in text.split(' by ', 1))
        link = next((a.get('title') for a in node.xpath('.//a[@title]') if text_of(a) == title), '')
    else:
        title, person = '', text
    if len(director.split()) > 6:
        director = ''
    return title, person, director, link


def grid(table):
    """Expand rowspan/colspan into a list of rows of (header?, cell element)."""
    rows, pending = [], {}
    for tr in table.xpath('.//tr'):
        row, col = [], 0
        cells = tr.xpath('./th|./td')
        while cells or col in pending:
            if col in pending:
                cell, left = pending.pop(col)
                row.append(cell)
                if left > 1:
                    pending[col] = (cell, left - 1)
                col += 1
                continue
            cell = cells.pop(0)
            span, down = int(cell.get('colspan', '1') or 1), int(cell.get('rowspan', '1') or 1)
            for _ in range(min(span, 20)):
                row.append(cell)
                if down > 1:
                    pending[col] = (cell, down - 1)
                col += 1
        rows.append(row)
    return rows


def headings(doc):
    """Yield (heading trail, element) for each top-level block in the article."""
    trail = {}
    root = doc.xpath('//div[contains(@class,"mw-parser-output")]')[0]
    for el in root:
        if 'mw-heading' in (el.get('class') or ''):
            h = el.xpath('./h2|./h3|./h4')
            if h:
                level = int(h[0].tag[1])
                trail = {k: v for k, v in trail.items() if k < level}
                trail[level] = text_of(h[0])
            continue
        yield [trail[k] for k in sorted(trail)], el


def year_of(*texts):
    for text in texts:
        match = YEAR.search(text or '')
        if match:
            return int(match.group(1)), (ORDINAL.search(text).group(1) if ORDINAL.search(text) else '')
    return None, ''


def extract(fest, page):
    """Return (entries, juries) from one article. entry = dict(year, number, award, title, person, director, link)."""
    import lxml.html
    doc = lxml.html.fromstring(page['html'])
    entries, juries = [], []
    for trail, el in headings(doc):
        heading = trail[-1] if trail else ''
        h_year, h_number = year_of(*reversed(trail))
        tables = [el] if el.tag == 'table' else el.xpath('.//table')
        for table in tables:
            if 'wikitable' not in (table.get('class') or ''):
                continue
            rows = grid(table)
            if not rows:
                continue
            head = [text_of(strip_refs(c)) for c in rows[0]]
            low = [h.lower() for h in head]
            body = [r for r in rows[1:] if any(c.tag == 'td' for c in r)]
            if any(h.startswith('jury') or 'jury members' in h for h in low):
                jcol = next(i for i, h in enumerate(low) if h.startswith('jury') or 'jury members' in h)
                last_year = None
                for r in body:
                    texts = [text_of(c) for c in r]
                    year, _ = year_of(texts[0], heading)
                    year = year or last_year
                    last_year = year
                    members = r[jcol] if len(r) > jcol else r[-1]
                    category = texts[1] if len(r) > 2 and len(texts) > 1 and r[1] is not members else texts[0]
                    names = [clean(n) for n in re.split(r',|\band\b', text_of(members))]
                    for name in names:
                        name = re.sub(r'\s*\([^)]*\)$', '', name)
                        if year and name and len(name.split()) <= 5:
                            juries.append((year, category if not YEAR.search(category) else 'Jury', name))
                continue
            first = low[0] if low else ''
            if first in {'ceremony', 'year', 'edition'} and len(head) > 2 and not any(k in low for k in ('film', 'winner', 'title')):
                # One row per edition, one column per award (Kolkata).
                for r in body:
                    year, number = year_of(text_of(r[0]))
                    for name, cell in zip(head[1:], r[1:]):
                        if 'source' in name.lower() or 'ref' in name.lower():
                            continue
                        got = parse_cell(cell)
                        if year and got:
                            entries.append(dict(year=year, number=number, award=clean(name.replace(' : ', ' · ')), **dict(zip(('title', 'person', 'director', 'link'), got))))
                continue
            # One row per award: Category | Winner, or Year | Film | Director.
            cat = next((i for i, h in enumerate(low) if h in {'category', 'award', 'section', 'prize'}), None)
            win = next((i for i, h in enumerate(low) if h.startswith(('winner', 'film', 'title', 'recipient'))), None)
            ycol = next((i for i, h in enumerate(low) if h in {'year', 'edition', 'ceremony'}), None)
            dcol = next((i for i, h in enumerate(low) if h.startswith('director')), None)
            if win is None:
                continue
            for r in body:
                if len(r) <= win:
                    continue
                year, number = year_of(text_of(r[ycol]) if ycol is not None else '', *reversed(trail))
                got = parse_cell(r[win])
                if not (year and got):
                    continue
                title, person, director, link = got
                if dcol is not None and len(r) > dcol:
                    director = text_of(strip_refs(r[dcol]))
                if not title and person and low[win].startswith(('film', 'title')):
                    title, person = person, ''
                award = text_of(r[cat]) if cat is not None else heading
                entries.append(dict(year=year, number=number or h_number, award=award, title=title, person=person, director=director, link=link))
        for li in el.xpath('./li|./ul/li') if el.tag in ('ul', 'ol') else []:
            # "2025: <i>Title</i> - Director | Country" under an award heading (KASHISH).
            text = text_of(strip_refs(li))
            match = re.match(r'^((?:19|20)\d\d)\s*[:–-]', text)
            if not match or not li.xpath('.//i'):
                continue
            li.text = re.sub(r'^\s*(?:19|20)\d\d\s*[:–-]\s*', '', li.text or '')
            got = parse_cell(li)
            if got:
                title, person, director, link = got
                if title and not person:
                    director = clean(re.sub(r'^\s*[-–]\s*', '', text.partition(title)[2]).split('|')[0])
                person = re.split(r'\s+(?:&|and)\s+', person)[0] if person else ''  # shortcut: keeps the first of several recipients
                entries.append(dict(year=int(match.group(1)), number='', award=heading, title=title, person=person, director=director if len(director.split()) <= 6 else '', link=link))
    return entries, juries


def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:40]


def build(cache, out=OUT):
    cache = Path(cache)
    films_wd = {}
    for b in json.loads((cache / 'films.json').read_text()) if (cache / 'films.json').exists() else []:
        rec = films_wd.setdefault(val(b, 't'), dict(qid=val(b, 'film'), kinds=set(), lang=[], country=[], dir=[], desc=val(b, 'desc'), year=None))
        rec['kinds'].add(val(b, 'kind'))
        for key, field in (('langLabel', 'lang'), ('countryLabel', 'country'), ('dirLabel', 'dir')):
            if val(b, key) and val(b, key) not in rec[field] and not re.match(r'^Q\d+$', val(b, key)):
                rec[field].append(val(b, key))
        if val(b, 'date'):
            rec['year'] = min(int(val(b, 'date')[:4]), rec['year'] or 9999)
    wd_editions = {}
    for b in json.loads((cache / 'editions.json').read_text()) if (cache / 'editions.json').exists() else []:
        year, _ = year_of(val(b, 'start'), val(b, 'date'), val(b, 'edLabel'))
        if year:
            wd_editions.setdefault(val(b, 'f'), {})[year] = dict(number=ORDINAL.search(val(b, 'edLabel')).group(1) if ORDINAL.search(val(b, 'edLabel')) else '', qid=val(b, 'ed'))
    world = ROOT / 'world-festivals.json'
    logos = {r['id']: r['logo'] for r in json.loads(world.read_text())['festivals'] if r.get('logo')} if world.exists() else {}
    festivals, films, honors = [], {}, []
    for fest in FESTIVALS:
        path = cache / 'wiki' / f"{fest['id']}.json"
        if not path.exists():
            continue
        page = json.loads(path.read_text())
        source = f"https://en.wikipedia.org/w/index.php?title={urllib.parse.quote(page['title'].replace(' ', '_'))}&oldid={page['revid']}"
        entries, juries = extract(fest, page)
        years = {}
        for e in entries:
            if e['number']:
                years[e['year']] = e['number']
            years.setdefault(e['year'], '')
        for year, info in wd_editions.get(fest['wikidata'], {}).items():
            if not years.get(year):
                years[year] = info['number']
        for year, _, _ in juries:
            years.setdefault(year, '')
        if not entries:
            continue  # nothing extractable yet: the festival stays on the work-in-progress list
        jury_by_year = {}
        for year, category, name in juries:
            jury_by_year.setdefault(year, []).append([category, name])
        editions = [dict(year=y, **({'number': n} if n else {}), source=source, **({'jury': jury_by_year[y]} if y in jury_by_year else {})) for y, n in sorted(years.items(), reverse=True)]
        festivals.append(dict(id=fest['id'], short=fest['short'], name=fest.get('name', fest['wiki']), region=fest['region'], country='India',
                              description=fest['description'], wikidata=fest['wikidata'], **({'url': fest['url']} if fest.get('url') else {}),
                              lat=fest['lat'], lon=fest['lon'], source=source, **({'logo': logos[fest['wikidata']]} if fest['wikidata'] in logos else {}), editions=editions))
        for e in entries:
            if not e['title']:
                if e['person'] and e['person'] != e['award'] and len(e['person'].split()) <= 8:
                    for person in re.split(r'\s+(?:&|and)\s+', e['person']):
                        honors.append(dict(festival=fest['id'], year=e['year'], award=[e['award'], source, clean(person)], role=role_for(e['award']) or 'Honoree'))
                continue
            wd = films_wd.get(e['link']) if e['link'] else None
            key = (fest['id'], e['year'], slug(e['title']))
            film = films.get(key)
            if not film:
                kinds = wd['kinds'] if wd else set()
                low = e['award'].lower()
                fmt = 'Documentary' if 'Q93204' in kinds or 'documentary' in low else 'Short film' if 'Q24862' in kinds or 'short' in low else fest.get('format', 'Feature')
                film = films[key] = dict(id=f"in-{fest['id']}-{e['year']}-{slug(e['title'])}", title=e['title'], festival=fest['id'], year=e['year'], format=fmt,
                                         **({'language': ', '.join(wd['lang'])} if wd and wd['lang'] else {}),
                                         **({'country': ', '.join(wd['country'])} if wd and wd['country'] else {}),
                                         **({'summary': wd['desc'][0].upper() + wd['desc'][1:] + '.'} if wd and wd['desc'] else {}),
                                         **({'wikidata': wd['qid']} if wd else {}),
                                         credits=[], awards=[], sources=[source])
                for name in (wd['dir'] if wd else []):
                    film['credits'].append(['Director', name])
            if e['director'] and not any(r == 'Director' for r, _ in film['credits']):
                for name in re.split(r',\s*|\s+(?:&|and)\s+', e['director']):
                    if clean(name)[:1].isupper():  # drops trailing notes such as "executive producer X"
                        film['credits'].append(['Director', clean(name)])
            award = [e['award'], source] + ([e['person']] if e['person'] else [])
            if award not in film['awards']:
                film['awards'].append(award)
            role = role_for(e['award'])
            if e['person'] and role and [role, e['person']] not in film['credits']:
                film['credits'].append([role, e['person']])
    shard = dict(
        about='Indian film festivals extracted by tools/extractors/india/extract.py from English Wikipedia and Wikidata. Facts only; each record links its source revision.',
        licence='Wikidata CC0; facts drawn from English Wikipedia (CC BY-SA 4.0), attributed by source link.',
        festivals=festivals, films=sorted(films.values(), key=lambda f: (f['festival'], -f['year'], f['title'])), honors=honors)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(shard, ensure_ascii=False, indent=1) + '\n')
    print(f"{out}: {len(festivals)} festivals, {sum(len(f['editions']) for f in festivals)} editions, {len(films)} films, {len(honors)} honours")


def role_for(award):
    low = award.lower()
    return 'Director' if re.search(r'best direct|direct(or|ion)$', low) else 'Actor' if re.search(r'\bact(or|ress|ing)\b|performance', low) else 'Writer' if 'screenplay' in low else ''


def test():
    import lxml.html
    cell = lambda h: parse_cell(lxml.html.fragment_fromstring(f'<td>{h}</td>'))
    assert cell('<a title="La Llorona (2019 film)"><i><b>La llorona</b></i></a><p>by</p><p>Jayro Bustamante</p>') == ('La llorona', '', 'Jayro Bustamante', 'La Llorona (2019 film)')
    assert cell('Indrasis Acharya <p>for</p><p><i><b>The Parcel</b></i></p>') == ('The Parcel', 'Indrasis Acharya', '', '')
    assert cell('<a title="Prabhu Solomon">Prabhu Solomon</a> for <a title="Mynaa">Mynaa</a>') == ('Mynaa', 'Prabhu Solomon', '', 'Mynaa')
    assert cell('<i>Kirumi</i> directed by Anucharan') == ('Kirumi', '', 'Anucharan', '')
    assert cell('<b>To the West, in Za</b><b>pata</b><p>by</p><p>David Bim</p>') == ('To the West, in Zapata', '', 'David Bim', '')
    assert cell('<i>Ana Endara</i><p>for</p><p><i><a title="Beloved Tropic"><b>Beloved Tropic</b></a></i></p>') == ('Beloved Tropic', 'Ana Endara', '', 'Beloved Tropic')
    assert cell('Nayanthara') == ('', 'Nayanthara', '', '')
    assert cell('') is None
    assert role_for('Director K.Balachander Award') == '' and role_for('IMI · Best Director') == 'Director'
    assert year_of('25th Kolkata International Film Festival (2019)') == (2019, '25th')
    print('ok')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'fetch':
        fetch(sys.argv[2])
    elif cmd == 'build':
        build(sys.argv[2])
    elif cmd == 'test':
        test()
    elif not cmd:
        fetch(ROOT / '.cache' / 'india')
        build(ROOT / '.cache' / 'india')
    else:
        sys.exit(__doc__)
