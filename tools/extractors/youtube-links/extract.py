#!/usr/bin/env python3
"""Link catalogue films to YouTube videos recorded on Wikidata (P1651).

Usage: python3 tools/extractors/youtube-links/extract.py [cache-dir]
Matches by title, year within two and the director (or country when the catalogue has no director),
then writes data/youtube-links/youtube.json: {catalogue film id: {wikidata, youtube: [[video id, 'trailer' | 'video'], ...]}}.
The app merges it into the catalogue when it loads.
"""
import collections, json, os, re, sys, unicodedata, urllib.parse, urllib.request

ENDPOINT = 'https://query.wikidata.org/sparql'
FILMS_WITH_VIDEO = '''SELECT ?f ?label ?year WHERE {
  ?f wdt:P1651 ?yt ; wdt:P31/wdt:P279* wd:Q11424 ; rdfs:label ?label .
  FILTER(LANG(?label) IN ("en", "mul"))
  OPTIONAL { ?f wdt:P577 ?d . BIND(YEAR(?d) AS ?year) }
}'''
DETAILS = '''SELECT ?f ?yt ?roleLabel ?dirLabel ?countryLabel WHERE {
  VALUES ?f { %s }
  ?f p:P1651 ?st . ?st ps:P1651 ?yt . OPTIONAL { ?st pq:P3831 ?role }
  OPTIONAL { ?f wdt:P57 ?dir } OPTIONAL { ?f wdt:P495 ?country }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}'''


def sparql(query, cache, name):
    path = os.path.join(cache, name)
    if not os.path.exists(path):
        request = urllib.request.Request(ENDPOINT, data=urllib.parse.urlencode({'query': query}).encode(),
                                         headers={'Accept': 'application/sparql-results+json', 'User-Agent': 'filmfest-guide-import/1.0'})
        with urllib.request.urlopen(request, timeout=120) as reply, open(path, 'wb') as out:
            out.write(reply.read())
    return json.load(open(path))['results']['bindings']


def key(text):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', text.lower()))


def person(text):
    return ' '.join(sorted(key(part) for part in text.split()))  # name order differs between sources


def qid(binding):
    return binding['f']['value'].rsplit('/', 1)[1]


def main(cache):
    os.makedirs(cache, exist_ok=True)
    years, by_title = collections.defaultdict(set), collections.defaultdict(set)
    for b in sparql(FILMS_WITH_VIDEO, cache, 'yt-films.json'):
        by_title[key(b['label']['value'])].add(qid(b))
        if 'year' in b:
            years[qid(b)].add(int(b['year']['value']))

    catalog = json.load(open('catalog.json'))
    near = lambda q, year, gap: any(abs(y - year) <= gap for y in years[q])
    candidates = {q for film in catalog['films'] for q in by_title.get(key(film['title']), ()) if near(q, film['year'], 2)}
    directors, countries, videos = (collections.defaultdict(set) for _ in range(3))
    roles = {}
    for b in sparql(DETAILS % ' '.join('wd:' + q for q in sorted(candidates)), cache, 'yt-details.json'):
        q, video = qid(b), b['yt']['value']
        videos[q].add(video)
        if 'trailer' in b.get('roleLabel', {}).get('value', ''):
            roles[video] = 'trailer'
        if 'dirLabel' in b:
            directors[q].add(person(b['dirLabel']['value']))
        if 'countryLabel' in b:
            countries[q].add(key(b['countryLabel']['value']))

    links = {}
    for film in catalog['films']:
        made_by = {person(name) for role, name in film['credits'] if 'direct' in role.lower()}
        made_in = {key(c) for c in (film.get('country') or '').split(', ') if c}
        for q in sorted(by_title.get(key(film['title']), ())):
            if not near(q, film['year'], 2):
                continue
            if made_by and directors[q]:
                ok = bool(made_by & directors[q])
            else:
                ok = bool(made_in & countries[q]) and near(q, film['year'], 1)
            if ok:
                links[film['id']] = {'wikidata': q, 'youtube': [[video, roles.get(video, 'video')] for video in sorted(videos[q], key=lambda v: (roles.get(v) != 'trailer', v))]}
                break
    os.makedirs('data/youtube-links', exist_ok=True)
    json.dump({'source': 'Wikidata (CC0), property P1651', 'count': len(links), 'films': dict(sorted(links.items()))}, open('data/youtube-links/youtube.json', 'w'), ensure_ascii=False, indent=1)
    print(f'{len(links)} films linked to YouTube')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.cache/youtube-links')
