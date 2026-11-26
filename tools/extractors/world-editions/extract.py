"""World festivals extractor: editions, winners and nominated films from Wikidata.

    python3 tools/extractors/world-editions/extract.py            # writes data/world-editions/catalog.json
    python3 tools/extractors/world-editions/extract.py --check    # self-test only, no network

Covers major festivals outside the Big Five (Cannes, Venice, Berlin, TIFF and Sundance have their own extractor).
The shard has the catalog.json shape and is listed in data/shards.json. Festival ids are Wikidata QIDs, so an
imported festival replaces its entry from world-festivals.json.

Source and licence: everything comes from Wikidata (CC0). Each record links to its Wikidata item and,
where one exists, its English Wikipedia article. No Wikipedia text is copied.
"""
import json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(ROOT, 'data', 'world-editions', 'catalog.json')
UA = {'User-Agent': 'filmfest-guide-data/1.0 (open data project; github.com/omshivaprakash/filmfest-guide)',
      'Accept': 'application/sparql-results+json'}
FESTIVALS = {
    'Q502053': 'Locarno', 'Q622423': 'San Sebastián', 'Q1666554': 'IFFR', 'Q332869': 'KVIFF', 'Q482633': 'BIFF Busan',
    'Q1043431': 'TIFF Tokyo', 'Q477369': 'SIFF Shanghai', 'Q949173': 'Mar del Plata', 'Q749235': 'MIFF Moscow',
    'Q935127': 'Sarajevo', 'Q2402350': 'Telluride', 'Q853325': 'Tribeca', 'Q959755': 'SXSW', 'Q5909927': 'Hot Docs',
    'Q1408677': 'Annecy', 'Q465682': 'Clermont-Ferrand', 'Q1666506': 'IDFA', 'Q1323689': 'BFI London', 'Q25648': 'NYFF',
    'Q3046725': 'Black Nights', 'Q1576451': 'Thessaloniki', 'Q1025968': 'Cairo', 'Q2545738': 'Carthage',
    'Q1202380': 'FESPACO', 'Q1559713': 'Göteborg', 'Q1578899': 'Warsaw', 'Q975945': 'Sitges', 'Q3070717': 'Marrakech',
    'Q141108': 'Fajr', 'Q260979': 'Sydney', 'Q5252683': 'MIFF Melbourne', 'Q1189150': 'HKIFF', 'Q1408552': 'Guadalajara',
    'Q3070714': 'Morelia', 'Q1284745': 'Edinburgh', 'Q1071936': 'Chicago', 'Q2399132': 'Seattle', 'Q1374050': 'Palm Springs',
    'Q63224859': 'Red Sea',  # Kolkata is in the india extractor
}
# Hand-listed festivals in catalog.json whose names differ from Wikidata's.
HAND_IDS = {'Q949173': 'mardelplata', 'Q959755': 'sxsw', 'Q1202380': 'fespaco', 'Q1559713': 'goteborg', 'Q3070717': 'marrakech'}
# Main prizes whose Wikidata items are not linked back to their festival.
EXTRA_AWARDS = {'Q38842580': 'Q749235'}  # Golden George, Moscow
FORMATS = {'Q24862': 'Short film', 'Q93204': 'Documentary', 'Q11424': 'Feature', 'Q24869': 'Feature', 'Q202866': 'Feature'}
UNLISTED = 'Format unlisted'
WD = 'https://www.wikidata.org/wiki/'
MONTHS = 'January February March April May June July August September October November December'.split()


def sparql(query, tries=5):
    data = urllib.parse.urlencode({'query': query}).encode()
    for attempt in range(tries):
        try:
            reply = urllib.request.urlopen(urllib.request.Request('https://query.wikidata.org/sparql', data, UA), timeout=120)
            time.sleep(1)  # stay well under the query service limits
            return json.load(reply)['results']['bindings']
        except Exception as error:  # 429, 5xx and timeouts: back off and retry
            print('retry', attempt + 1, error, file=sys.stderr)
            time.sleep(10 * (attempt + 1))
    raise SystemExit('Wikidata query failed; keeping the existing shard')  # never overwrite good data with a partial run


def val(row, key):
    value = row.get(key, {}).get('value')
    return value.rsplit('/', 1)[1] if value and value.startswith('http://www.wikidata.org/entity/') else value


def values(ids):
    return ' '.join('wd:' + i for i in ids)


def batched(ids, size=250):
    ids = sorted(ids)
    for i in range(0, len(ids), size):
        yield ids[i:i + size]


def ordinal(n):
    n = int(n)
    suffix = 'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f'{n}{suffix}'


def date_range(start, end):
    if not start or not end or start[:10] == end[:10] or start[5:10] == '01-01':
        return None  # year-only precision: no useful dates
    (y1, m1, d1), (y2, m2, d2) = (map(int, start[:10].split('-')), map(int, end[:10].split('-')))
    if m1 == m2:
        return f'{d1}–{d2} {MONTHS[m1 - 1]}'
    return f'{d1} {MONTHS[m1 - 1]}–{d2} {MONTHS[m2 - 1]}'


def sentence(text):
    return (text[:1].upper() + text[1:]) if text else ''


def year(row, *keys):
    for key in keys:
        if val(row, key) and re.match(r'^\d{4}', val(row, key)):
            return int(val(row, key)[:4])


def fetch():
    fests = values(FESTIVALS)
    editions = sparql(f'''SELECT ?fest ?e ?n ?start ?end ?point ?wiki WHERE {{ VALUES ?fest {{ {fests} }}
      {{ ?e wdt:P179 ?fest }} UNION {{ ?e wdt:P361 ?fest }} {{ ?e wdt:P393 ?n }} UNION {{ ?e wdt:P31 wd:Q27968055 }}
      OPTIONAL {{ ?e wdt:P580 ?start }} OPTIONAL {{ ?e wdt:P582 ?end }} OPTIONAL {{ ?e wdt:P585 ?point }}
      OPTIONAL {{ ?wiki schema:about ?e; schema:isPartOf <https://en.wikipedia.org/> }} }}''')
    awards = {val(r, 'a'): val(r, 'fest') for r in sparql(
        f'SELECT DISTINCT ?a ?fest WHERE {{ VALUES ?fest {{ {fests} }} ?a (wdt:P1027|wdt:P361)+ ?fest . }}')}
    awards.update(EXTRA_AWARDS)
    labels, results = {}, []
    for chunk in batched(awards):
        for prop, kind in (('P166', 'win'), ('P1411', 'nom')):
            for r in sparql(f'''SELECT ?a ?aLabel ?s ?t ?edt WHERE {{ VALUES ?a {{ {values(chunk)} }} ?s p:{prop} ?st . ?st ps:{prop} ?a .
              OPTIONAL {{ ?st pq:P585 ?t }} OPTIONAL {{ ?st pq:P805 ?ed . ?ed wdt:P585|wdt:P580 ?edt }}
              SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en,mul,fr,es,de". }} }}'''):
                labels[val(r, 'a')] = val(r, 'aLabel')
                results.append({'award': val(r, 'a'), 'subject': val(r, 's'), 'year': year(r, 't', 'edt'), 'kind': kind})
    subjects = {}
    for chunk in batched({r['subject'] for r in results}):
        for r in sparql(f'''SELECT ?s ?sLabel ?sDescription ?type ?dirLabel ?countryLabel ?langLabel ?wiki WHERE {{ VALUES ?s {{ {values(chunk)} }}
          OPTIONAL {{ ?s wdt:P31 ?type }} OPTIONAL {{ ?s wdt:P57 ?dir }} OPTIONAL {{ ?s wdt:P495 ?country }} OPTIONAL {{ ?s wdt:P364 ?lang }}
          OPTIONAL {{ ?wiki schema:about ?s; schema:isPartOf <https://en.wikipedia.org/> }}
          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en,mul,fr,es,de". }} }}'''):
            s = subjects.setdefault(val(r, 's'), {'label': val(r, 'sLabel'), 'desc': val(r, 'sDescription'), 'wiki': val(r, 'wiki'),
                                                  'types': [], 'directors': [], 'countries': [], 'languages': []})
            for key, field in (('type', 'types'), ('dirLabel', 'directors'), ('countryLabel', 'countries'), ('langLabel', 'languages')):
                if val(r, key) and val(r, key) not in s[field]:
                    s[field].append(val(r, key))
    for s in subjects.values():  # stable output, so unchanged data commits nothing
        for field in ('types', 'directors', 'countries', 'languages'):
            s[field].sort()
    return {'editions': editions, 'awards': awards, 'labels': labels, 'results': results, 'subjects': subjects}


def build(raw, world, hand):
    eds = {}
    for r in raw['editions']:
        y = year(r, 'start', 'point')
        if not y:
            continue
        ed = eds.setdefault(val(r, 'fest'), {}).setdefault(y, {'year': y})
        if val(r, 'n') and val(r, 'n').isdigit():
            ed['number'] = ordinal(val(r, 'n'))
        if date_range(val(r, 'start'), val(r, 'end')):
            ed['dates'] = date_range(val(r, 'start'), val(r, 'end'))
        ed['source'] = val(r, 'wiki') or WD + val(r, 'e')
    films, honors = {}, []
    for r in raw['results']:
        s, fest = raw['subjects'].get(r['subject']), raw['awards'][r['award']]
        name = raw['labels'].get(r['award'])
        if not r['year'] or not s or not name or re.match(r'^Q\d+$', s['label'] or 'Q') or re.match(r'^Q\d+$', name):
            continue  # undated, or no usable label
        eds.setdefault(fest, {}).setdefault(r['year'], {'year': r['year'], 'source': WD + fest})
        award = [name if r['kind'] == 'win' else f'Nominated: {name}', WD + r['award']]
        if 'Q5' in s['types']:
            if r['kind'] == 'win':
                honors.append({'festival': fest, 'year': r['year'], 'award': award + [s['label']], 'role': 'Honoree',
                               'sources': [WD + r['subject']] + ([s['wiki']] if s['wiki'] else [])})
            continue
        key = f"{r['subject']}-{fest}-{r['year']}".lower()
        film = films.setdefault(key, {
            'id': key, 'title': s['label'], 'festival': fest, 'year': r['year'],
            'format': next((FORMATS[t] for t in s['types'] if t in FORMATS), UNLISTED),
            'language': ', '.join(s['languages']), 'country': ', '.join(s['countries']),
            'summary': sentence(s['desc']), 'credits': [['Director', d] for d in s['directors']],
            'awards': [], 'sources': [WD + r['subject']] + ([s['wiki']] if s['wiki'] else []), 'wikidata': r['subject']})
        if award not in film['awards']:
            film['awards'].append(award)
    for film in films.values():  # wins before nominations
        film['awards'].sort(key=lambda a: (a[0].startswith('Nominated'), a[0]))
    festivals = []
    for qid, short in FESTIVALS.items():
        if not eds.get(qid):
            continue
        w = world.get(qid, {})
        record = {'id': hand.get(w.get('name'), (qid,))[0], 'wikidata': qid, 'short': hand.get(w.get('name'), (qid, short))[1], 'name': w.get('name', short), 'region': w.get('region', ''), 'country': w.get('country'), 'city': w.get('city'),
                  'lat': (w.get('ll') or [None, None])[1], 'lon': (w.get('ll') or [None])[0],
                  'description': sentence(w.get('desc')), 'url': re.sub(r'^http://', 'https://', w.get('url') or ''),  # the site check requires https 'wiki': w.get('wiki'),
                  'editions': sorted(eds[qid].values(), key=lambda e: -e['year'])}
        if w.get('logo'):
            record['logo'] = w['logo']
        festivals.append({k: v for k, v in record.items() if v is not None and v != ''})
    ids = {f['wikidata']: f['id'] for f in festivals}
    for record in [*films.values(), *honors]:
        record['festival'] = ids.get(record['festival'], record['festival'])
    return {'source': 'Wikidata (CC0). Each record links to its Wikidata item and English Wikipedia article.',
            'license': 'CC0 1.0', 'extractor': 'tools/extractors/world-editions/extract.py',
            'festivals': festivals, 'films': sorted(films.values(), key=lambda f: (f['festival'], -f['year'], f['title'], f['id'])),
            'honors': sorted(honors, key=lambda h: (h['festival'], -h['year'], h['award'][2], h['award'][0]))}


def check():
    assert [ordinal(n) for n in (1, 2, 3, 4, 11, 12, 13, 21, 22, 111)] == ['1st', '2nd', '3rd', '4th', '11th', '12th', '13th', '21st', '22nd', '111th']
    assert date_range('2010-08-04T00:00:00Z', '2010-08-14T00:00:00Z') == '4–14 August'
    assert date_range('2010-07-30T00:00:00Z', '2010-08-09T00:00:00Z') == '30 July–9 August'
    assert date_range('2010-01-01T00:00:00Z', '2010-12-31T00:00:00Z') is None
    e = 'http://www.wikidata.org/entity/'
    raw = {'editions': [{'fest': {'value': e + 'Q502053'}, 'e': {'value': e + 'Q1'}, 'n': {'value': '63'}, 'start': {'value': '2010-08-04T00:00:00Z'}}],
           'awards': {'Q9': 'Q502053'}, 'labels': {'Q9': 'Golden Leopard'},
           'results': [{'award': 'Q9', 'subject': 'Q7', 'year': 2010, 'kind': 'nom'}, {'award': 'Q9', 'subject': 'Q7', 'year': 2010, 'kind': 'win'},
                       {'award': 'Q9', 'subject': 'Q8', 'year': None, 'kind': 'win'}],
           'subjects': {'Q7': {'label': 'Film', 'desc': 'a film', 'wiki': None, 'types': ['Q11424'], 'directors': ['D'], 'countries': [], 'languages': []}}}
    out = build(raw, {}, {})
    assert out['festivals'][0]['editions'] == [{'year': 2010, 'number': '63rd', 'source': WD + 'Q1'}]
    assert len(out['films']) == 1 and out['films'][0]['awards'][0][0] == 'Golden Leopard' and out['films'][0]['format'] == 'Feature'
    assert sentence('1998 film directed by Bille August') == '1998 film directed by Bille August'
    print('self-check passed')


if __name__ == '__main__':
    check()
    if '--check' not in sys.argv:
        world = {r['id']: r for r in json.load(open(os.path.join(ROOT, 'world-festivals.json')))['festivals']}
        # A hand-listed festival keeps its id, so the app drops its work-in-progress entry.
        listed = json.load(open(os.path.join(ROOT, 'catalog.json'))).get('worldFestivals', [])
        hand = {r['name']: (r['id'], r.get('short') or r['name']) for r in listed}
        for qid, slug in HAND_IDS.items():
            r = next(r for r in listed if r['id'] == slug)
            hand[world[qid]['name']] = (slug, r.get('short') or r['name'])
        out = build(fetch(), world, hand)
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, 'w') as f:
            json.dump(out, f, ensure_ascii=False, separators=(',', ':'))
            f.write('\n')
        print(f"{len(out['festivals'])} festivals, {sum(len(x['editions']) for x in out['festivals'])} editions, "
              f"{len(out['films'])} films, {len(out['honors'])} honours -> {os.path.relpath(OUT, ROOT)}")
