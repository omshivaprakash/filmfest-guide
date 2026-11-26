#!/usr/bin/env python3
"""Build data/world-editions/world-films.json: editions, award winners and selected films of the best-known world festivals.

Usage: python3 tools/extractors/world-editions/extract.py [cache-dir] [how many festivals, default 40]
Takes the festivals with the most Wikipedia language editions from data/world-festivals/, then asks Wikidata for
their editions (Q27787439), the films that won or were nominated for their awards (P166, P1411) and the films
presented at each edition (P13360, or P1344 on the film). Data from Wikidata is CC0.
"""
import collections, json, os, re, sys, time, urllib.parse, urllib.request

ENDPOINT = 'https://query.wikidata.org/sparql'
EDITION = 'Q27787439'


def sparql(query, cache, name):
    path = os.path.join(cache, name)
    if not os.path.exists(path):
        for attempt in range(4):
            try:
                request = urllib.request.Request(ENDPOINT, data=urllib.parse.urlencode({'query': query}).encode(),
                                                 headers={'Accept': 'application/sparql-results+json', 'User-Agent': 'filmfest-guide-import/1.0'})
                with urllib.request.urlopen(request, timeout=120) as reply:
                    data = reply.read()
                json.loads(data)
                open(path, 'wb').write(data)
                break
            except Exception as error:  # rate limits and timeouts: wait and retry
                print('retry', name, error, file=sys.stderr)
                time.sleep(15 * (attempt + 1))
        else:
            return []
        time.sleep(1)
    return json.load(open(path))['results']['bindings']


def qid(binding, key):
    return binding[key]['value'].rsplit('/', 1)[1] if key in binding else None


def text(binding, key):
    return binding.get(key, {}).get('value')


def year(value):
    match = re.match(r'(-?\d{4})', value or '')
    return int(match[1]) if match else None


def main(cache, count=40):
    os.makedirs(cache, exist_ok=True)
    world = json.load(open('data/world-festivals/world-festivals.json'))['festivals']
    chosen = world[:count]
    out, film_ids = {}, set()
    for fest in chosen:
        f = fest['id']
        editions = {}
        for b in sparql(f'''SELECT ?e ?n ?start ?end ?pit WHERE {{ ?e wdt:P179|wdt:P361 wd:{f} ; wdt:P31 wd:{EDITION} .
            OPTIONAL {{ ?e wdt:P393 ?n }} OPTIONAL {{ ?e wdt:P580 ?start }} OPTIONAL {{ ?e wdt:P582 ?end }} OPTIONAL {{ ?e wdt:P585 ?pit }} }}''', cache, f'{f}-editions.json'):
            e = qid(b, 'e')
            when = year(text(b, 'start')) or year(text(b, 'pit'))
            if when:
                editions.setdefault(e, {'year': when, 'n': text(b, 'n'), 'start': (text(b, 'start') or '')[:10], 'end': (text(b, 'end') or '')[:10]})
        awards = '''{ ?a wdt:P1027|wdt:P361 wd:%s } UNION { ?a wdt:P31 ?cls . ?cls wdt:P1027|wdt:P361 wd:%s }
            FILTER NOT EXISTS { ?a wdt:P31 wd:%s }''' % (f, f, EDITION)
        entries = collections.OrderedDict()

        def add(film, when, kind, award=None):
            if not film or not when or when > int(time.strftime('%Y')):
                return
            film_ids.add(film)
            key = (film, when)
            entry = entries.setdefault(key, {'film': film, 'year': when, 'kind': kind, 'awards': []})
            rank = {'won': 0, 'nominated': 1, 'selected': 2}
            if rank[kind] < rank[entry['kind']]:
                entry['kind'] = kind
            if award and kind == 'won' and award not in entry['awards']:
                entry['awards'].append(award)

        def first_release(rows):
            # Without a date on the award, the film's earliest release (usually its festival premiere) gives the year.
            earliest = {}
            for b in rows:
                y = year(text(b, 'filmDate'))
                if y and (qid(b, 'film') not in earliest or y < earliest[qid(b, 'film')]):
                    earliest[qid(b, 'film')] = y
            return earliest

        won = sparql(f'''SELECT ?film ?aLabel ?date ?filmDate WHERE {{ {awards} ?film p:P166 ?st . ?st ps:P166 ?a . ?film wdt:P31/wdt:P279* wd:Q11424 .
            OPTIONAL {{ ?st pq:P585 ?date }} OPTIONAL {{ ?film wdt:P577 ?filmDate }}
            SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }} }}''', cache, f'{f}-won.json')
        earliest = first_release(won)
        for b in won:
            add(qid(b, 'film'), year(text(b, 'date')) or earliest.get(qid(b, 'film')), 'won', text(b, 'aLabel'))
        nominated = sparql(f'''SELECT ?film ?date ?filmDate WHERE {{ {awards} ?film p:P1411 ?st . ?st ps:P1411 ?a . ?film wdt:P31/wdt:P279* wd:Q11424 .
            OPTIONAL {{ ?st pq:P585 ?date }} OPTIONAL {{ ?film wdt:P577 ?filmDate }} }}''', cache, f'{f}-nominated.json')
        earliest = first_release(nominated)
        for b in nominated:
            add(qid(b, 'film'), year(text(b, 'date')) or earliest.get(qid(b, 'film')), 'nominated')
        for b in sparql(f'''SELECT DISTINCT ?film ?e WHERE {{ ?e wdt:P179|wdt:P361 wd:{f} ; wdt:P31 wd:{EDITION} .
            {{ ?e wdt:P13360 ?film }} UNION {{ ?film wdt:P1344 ?e }} ?film wdt:P31/wdt:P279* wd:Q11424 . }}''', cache, f'{f}-selected.json'):
            edition = editions.get(qid(b, 'e'))
            add(qid(b, 'film'), edition and edition['year'], 'selected')
        out[f] = {'editions': sorted(([e['year'], e['n'], e['start'], e['end']] for e in editions.values()), reverse=True),
                  'films': sorted(([e['film'], e['year'], e['kind'], sorted(e['awards'])] for e in entries.values()), key=lambda r: (-r[1], r[2], r[0]))}
        print(fest['name'], len(editions), 'editions', len(entries), 'films', file=sys.stderr)

    films = {}
    ids = sorted(film_ids)
    for i in range(0, len(ids), 250):
        values = ' '.join('wd:' + x for x in ids[i:i + 250])
        for b in sparql(f'''SELECT ?f ?fLabel ?date ?dirLabel ?countryLabel ?yt WHERE {{ VALUES ?f {{ {values} }}
            OPTIONAL {{ ?f wdt:P577 ?date }} OPTIONAL {{ ?f wdt:P57 ?dir }} OPTIONAL {{ ?f wdt:P495 ?country }} OPTIONAL {{ ?f wdt:P1651 ?yt }}
            SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en,mul,fr,es,de,it,ja". }} }}''', cache, f'films-{i}.json'):
            f = qid(b, 'f')
            row = films.setdefault(f, {'title': text(b, 'fLabel'), 'year': None, 'directors': [], 'countries': [], 'youtube': []})
            y = year(text(b, 'date'))
            if y and (not row['year'] or y < row['year']):
                row['year'] = y
            for key, field in (('directors', 'dirLabel'), ('countries', 'countryLabel'), ('youtube', 'yt')):
                value = text(b, field)
                if value and not re.fullmatch(r'Q\d+', value) and value not in row[key]:
                    row[key].append(value)
    films = {k: v for k, v in films.items() if v['title'] and not re.fullmatch(r'Q\d+', v['title'])}
    for fest in out.values():
        fest['films'] = [row for row in fest['films'] if row[0] in films]
    compact = {k: [v['title'], v['year'], sorted(v['directors']), sorted(v['countries'])] + ([sorted(v['youtube'])] if v['youtube'] else []) for k, v in sorted(films.items())}
    json.dump({'source': 'Wikidata (CC0)', 'retrieved': time.strftime('%Y-%m-%d'), 'count': len(compact), 'festivals': out, 'films': compact},
              open('data/world-editions/world-films.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    print(len(out), 'festivals,', len(compact), 'films,', sum(len(v['films']) for v in out.values()), 'festival entries')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.cache/world-editions', int(sys.argv[2]) if len(sys.argv) > 2 else 40)
