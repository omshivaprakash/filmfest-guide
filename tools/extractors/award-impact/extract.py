#!/usr/bin/env python3
"""What festival award winners went on to win: every award and nomination Wikidata records for them.

Usage: python3 tools/extractors/award-impact/extract.py [cache-dir]
Takes films in the guide (catalog.json and the shards in data/shards.json) that won a festival award and carry
a Wikidata id (their own, or one the youtube-links extractor matched), then reads "award received" (P166) and
"nominated for" (P1411) with their "point in time" (P585) year. Writes data/award-impact/impact.json:
{count, films: {QID: {won: [[award, award QID, year|null]], nominated: [...]}}}. Only what Wikidata records; nothing is inferred.
"""
import json, os, pathlib, sys, time, urllib.parse, urllib.request

ENDPOINT = 'https://query.wikidata.org/sparql'
QUERY = '''SELECT ?f ?kind ?a ?aLabel ?year WHERE {
  VALUES ?f { %s }
  VALUES (?p ?ps ?kind) { (p:P166 ps:P166 "won") (p:P1411 ps:P1411 "nominated") }
  ?f ?p ?st . ?st ?ps ?a .
  OPTIONAL { ?st pq:P585 ?d . BIND(YEAR(?d) AS ?year) }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,mul". }
}'''


def sparql(query, cache, name):
    path = os.path.join(cache, name)
    if not os.path.exists(path):
        for wait in (5, 30, 90, None):
            try:
                request = urllib.request.Request(ENDPOINT, data=urllib.parse.urlencode({'query': query}).encode(),
                                                 headers={'Accept': 'application/sparql-results+json', 'User-Agent': 'filmfest-guide-import/1.0'})
                with urllib.request.urlopen(request, timeout=120) as reply:
                    body = reply.read()
                break
            except OSError:
                if wait is None:
                    raise
                time.sleep(wait)
        pathlib.Path(path).write_bytes(body)
    return json.load(open(path))['results']['bindings']


def winners():
    films = json.load(open('catalog.json'))['films']
    for shard in json.load(open('data/shards.json')):
        if os.path.exists(shard):
            films += json.load(open(shard)).get('films', [])
    links = json.load(open('data/youtube-links/youtube.json'))['films']
    return sorted({film.get('wikidata') or links.get(film['id'], {}).get('wikidata') for film in films if film.get('awards')} - {None})


def main(cache):
    os.makedirs(cache, exist_ok=True)
    qids = winners()
    out = {}
    for start in range(0, len(qids), 200):
        batch = qids[start:start + 200]
        for b in sparql(QUERY % ' '.join('wd:' + q for q in batch), cache, f'impact-{start}.json'):
            film, award = (b[k]['value'].rsplit('/', 1)[1] for k in ('f', 'a'))
            name = b['aLabel']['value']
            if name == award:  # no English label
                continue
            year = int(b['year']['value']) if 'year' in b else None
            row = out.setdefault(film, {'won': [], 'nominated': []})[b['kind']['value']]
            if [name, award, year] not in row:
                row.append([name, award, year])
    for record in out.values():
        for rows in record.values():
            rows.sort(key=lambda row: (row[2] or 9999, row[0]))
    assert len(out) > len(qids) // 4, f'only {len(out)} of {len(qids)} winners have awards on Wikidata; refusing to overwrite'
    target = pathlib.Path('data/award-impact')
    target.mkdir(parents=True, exist_ok=True)
    (target / 'impact.json').write_text(json.dumps({
        'source': 'Wikidata (CC0): award received (P166) and nominated for (P1411), with point in time (P585).',
        'extractor': 'tools/extractors/award-impact/extract.py',
        'count': len(out), 'films': dict(sorted(out.items()))}, ensure_ascii=False, separators=(',', ':')) + '\n')
    print(f'{len(out)} of {len(qids)} award-winning films have awards or nominations on Wikidata')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/tmp/award-impact-cache')
