"""Build world-festivals.json from Wikidata, Wikipedia and Wikimedia Commons.

    python3 tools/import-world-festivals.py fetch <cache-dir>   # query the sources (slow, polite, resumable)
    python3 tools/import-world-festivals.py build <cache-dir>   # write world-festivals.json, world-about.json and images/world/

Festivals are Wikidata items that are an instance of "film festival" (Q220505) or one of its
common subclasses, excluding single editions. Only festivals with a name and a country are kept.
Wikidata is CC0. Descriptions quoted from Wikipedia are CC BY-SA and are linked to their article.
Logos and images come only from Wikimedia Commons and keep their own licence, which is stored with each one.
"""
import html, json, os, re, subprocess, sys, time, urllib.parse, urllib.request

UA = {'User-Agent': 'filmfest-guide-data/1.0 (open data project; github.com/omshivaprakash/filmfest-guide)'}
CLASSES = 'wd:Q220505 wd:Q62018250 wd:Q115858865 wd:Q123980018 wd:Q114196733 wd:Q9259338 wd:Q1794431 wd:Q5287670 wd:Q105091183 wd:Q130745618 wd:Q109594423'
IN_GUIDE = re.compile(r'^(International Film Festival of India|Bengaluru International Film Festival|International Film Festival of Kerala|International Documentary and Short Film Festival of Kerala)$', re.I)
MIDDLE_EAST = {'Iran', 'Iraq', 'Israel', 'Jordan', 'Kuwait', 'Lebanon', 'Oman', 'Qatar', 'Saudi Arabia', 'Syria', 'United Arab Emirates', 'Yemen', 'Bahrain', 'State of Palestine', 'Palestine'}
NORTH = {'United States', 'Canada', 'Greenland'}
EXTRA_REGION = {'Hong Kong': 'Asia', 'Taiwan': 'Asia', 'Macau': 'Asia', 'Kosovo': 'Europe', 'Kingdom of the Netherlands': 'Europe', 'Puerto Rico': 'Latin America', 'Soviet Union': 'Europe', 'Yugoslavia': 'Europe', 'Czechoslovakia': 'Europe', 'West Germany': 'Europe', 'East Germany': 'Europe'}


def get(url, data=None, tries=6):
    for attempt in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, data=data, headers={**UA, 'Accept': 'application/json, application/sparql-results+json'}), timeout=90).read()
        except Exception as error:  # 429 and timeouts: back off and retry
            print('retry', url[:80], error, file=sys.stderr)
            time.sleep(5 * (attempt + 1))
    return None


def sparql(query):
    body = get('https://query.wikidata.org/sparql', urllib.parse.urlencode({'query': query}).encode())
    return json.loads(body)['results']['bindings'] if body else []


def value(binding, key):
    return binding.get(key, {}).get('value')


def fetch(cache):
    os.makedirs(cache, exist_ok=True)
    ids = {value(b, 'f').rsplit('/', 1)[1]: int(value(b, 'links')) for b in sparql(
        f'SELECT ?f ?links WHERE {{ VALUES ?c {{ {CLASSES} }} ?f wdt:P31 ?c . FILTER NOT EXISTS {{ ?f wdt:P31 wd:Q27968055 }} '
        'FILTER NOT EXISTS { ?f wdt:P179 [] } FILTER NOT EXISTS { ?f wdt:P393 [] } ?f wikibase:sitelinks ?links . }')}
    json.dump(ids, open(f'{cache}/ids.json', 'w'))
    details, wiki, keys = [], {}, sorted(ids)
    for i in range(0, len(keys), 300):
        values = ' '.join('wd:' + key for key in keys[i:i + 300])
        details += sparql(f'''SELECT ?f ?fLabel ?fDescription ?countryLabel ?placeLabel ?c1 ?c2 ?web ?logo ?inception WHERE {{
          VALUES ?f {{ {values} }}
          OPTIONAL {{ ?f wdt:P17 ?country }}
          OPTIONAL {{ ?f wdt:P276|wdt:P131|wdt:P159 ?place . OPTIONAL {{ ?place wdt:P625 ?c2 }} }}
          OPTIONAL {{ ?f wdt:P625 ?c1 }} OPTIONAL {{ ?f wdt:P856 ?web }} OPTIONAL {{ ?f wdt:P154 ?logo }} OPTIONAL {{ ?f wdt:P571 ?inception }}
          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en,mul,fr,es,de,it,pt,hi,ru,ja,zh". }} }}''')
        for b in sparql(f'SELECT ?f ?t WHERE {{ VALUES ?f {{ {values} }} ?a schema:about ?f ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?t . }}'):
            wiki[value(b, 'f').rsplit('/', 1)[1]] = value(b, 't')
        time.sleep(0.5)
    json.dump(details, open(f'{cache}/details.json', 'w'))
    json.dump(wiki, open(f'{cache}/enwiki.json', 'w'))
    json.dump(sparql('SELECT ?l ?c WHERE { ?k wdt:P31 wd:Q6256 ; wdt:P625 ?c ; rdfs:label ?l . FILTER(LANG(?l)="en") }'), open(f'{cache}/countries.json', 'w'))
    json.dump(sparql('SELECT ?l ?contLabel WHERE { ?k wdt:P31 wd:Q6256 ; wdt:P30 ?cont ; rdfs:label ?l . FILTER(LANG(?l)="en") SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } }'), open(f'{cache}/continents.json', 'w'))

    # Wikipedia: opening sentences and the page image, 20 titles per request.
    by_title, info = {t: q for q, t in wiki.items()}, {}
    titles = list(by_title)
    for i in range(0, len(titles), 20):
        body = get('https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode(dict(action='query', prop='pageimages|extracts', exintro=1, explaintext=1, exsentences=2, piprop='name', redirects=1, format='json', formatversion=2, titles='|'.join(titles[i:i + 20]))))
        query = json.loads(body).get('query', {}) if body else {}
        renamed = {x['to']: x['from'] for x in query.get('normalized', []) + query.get('redirects', [])}
        for page in query.get('pages', []):
            title = page.get('title')
            original = renamed.get(renamed.get(title, title), renamed.get(title, title))
            qid = by_title.get(original) or by_title.get(title)
            if qid:
                info[qid] = {'extract': page.get('extract'), 'image': page.get('pageimage'), 'title': title}
        time.sleep(1)
    json.dump(info, open(f'{cache}/wpinfo.json', 'w'))

    # Commons: licence, author and a 250px thumbnail for each logo or page image. Files that are not on Commons are skipped.
    logos = {}
    for b in details:
        qid, logo = value(b, 'f').rsplit('/', 1)[1], value(b, 'logo')
        if logo:
            logos.setdefault(qid, urllib.parse.unquote(logo.rsplit('/', 1)[1]).replace('_', ' '))
    for qid, page in info.items():
        if page.get('image'):
            logos.setdefault(qid, page['image'].replace('_', ' '))
    files, meta = sorted(set(logos.values())), {}
    for i in range(0, len(files), 40):
        body = get('https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(dict(action='query', prop='imageinfo', iiprop='url|extmetadata|mime', iiurlwidth=250, iiextmetadatafilter='LicenseShortName|LicenseUrl|Artist', format='json', formatversion=2, titles='|'.join('File:' + f for f in files[i:i + 40]))))
        for page in (json.loads(body).get('query', {}).get('pages', []) if body else []):
            if page.get('imageinfo'):
                ii, m = page['imageinfo'][0], page['imageinfo'][0].get('extmetadata', {})
                meta[page['title'][5:]] = {'thumb': ii.get('thumburl'), 'page': ii.get('descriptionurl'), 'mime': ii.get('mime'),
                                           'license': m.get('LicenseShortName', {}).get('value'), 'licenseUrl': m.get('LicenseUrl', {}).get('value'), 'artist': m.get('Artist', {}).get('value')}
        time.sleep(1)
    json.dump({'want': logos, 'meta': meta}, open(f'{cache}/images.json', 'w'))
    os.makedirs(f'{cache}/img', exist_ok=True)
    for qid, name in logos.items():
        m, out = meta.get(name), f'{cache}/img/{qid}.bin'
        if not m or not m.get('thumb') or not m['mime'].startswith('image/') or os.path.exists(out):
            continue
        data = get(m['thumb'].split('?')[0].replace('thumb.wikimedia.org', 'upload.wikimedia.org'), tries=5)
        if data:
            open(out, 'wb').write(data)
        time.sleep(1.2)


def point(text):
    match = re.match(r'Point\(([-\d.eE]+) ([-\d.eE]+)\)', text or '')
    return [round(float(match[1]), 3), round(float(match[2]), 3)] if match else None


def plain(text):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', text or ''))).strip()


FORMER = {'Czechoslovakia', 'Soviet Union', 'Yugoslavia', 'West Germany', 'East Germany', 'Socialist Federal Republic of Yugoslavia', 'Kingdom of Italy', 'Russian Empire', 'Serbia and Montenegro'}


def build(cache, root='.'):
    ids = json.load(open(f'{cache}/ids.json'))
    wp = json.load(open(f'{cache}/wpinfo.json'))
    wiki = json.load(open(f'{cache}/enwiki.json'))
    images = json.load(open(f'{cache}/images.json'))
    centres = {value(b, 'l'): point(value(b, 'c')) for b in json.load(open(f'{cache}/countries.json'))}
    continents = {}
    for b in json.load(open(f'{cache}/continents.json')):
        continents.setdefault(value(b, 'l'), []).append(value(b, 'contLabel'))

    def region(country):
        if country == 'India':
            return 'India'
        if country in EXTRA_REGION:
            return EXTRA_REGION[country]
        if country in MIDDLE_EAST:
            return 'Middle East'
        found = continents.get(country, [])
        for preferred in ('Europe', 'Africa', 'South America', 'North America', 'Asia', 'Indian subcontinent', 'Oceania', 'Insular Oceania', 'Eurasia'):
            if preferred in found:
                return {'South America': 'Latin America', 'North America': 'North America' if country in NORTH else 'Latin America',
                        'Indian subcontinent': 'Asia', 'Insular Oceania': 'Oceania', 'Eurasia': 'Europe'}.get(preferred, preferred)
        return 'Other'

    festivals = {}
    for b in json.load(open(f'{cache}/details.json')):
        qid = value(b, 'f').rsplit('/', 1)[1]
        row = festivals.setdefault(qid, {'id': qid})
        for key, field in (('name', 'fLabel'), ('desc', 'fDescription'), ('country', 'countryLabel'), ('city', 'placeLabel'), ('url', 'web')):
            text = value(b, field)
            if text and not re.fullmatch(r'Q\d+', text):
                if key == 'country' and row.get('country') in FORMER:
                    row['country'] = text  # prefer the present-day country
                row.setdefault(key, text)
        row.setdefault('ll', point(value(b, 'c1')) or point(value(b, 'c2')))
        year = re.match(r'-?\d+', value(b, 'inception') or '')
        if year:
            row.setdefault('since', int(year[0]))

    out_dir = os.path.join(root, 'images', 'world')
    os.makedirs(out_dir, exist_ok=True)
    result = []
    for qid, row in festivals.items():
        if not row.get('name') or not row.get('country') or IN_GUIDE.match(row['name']):
            continue
        if not row.get('ll'):
            if not centres.get(row['country']):
                continue
            row['ll'], row['approx'] = centres[row['country']], True  # placed at the country centre
        if not row['ll']:
            del row['ll']
        row['region'] = region(row['country'])
        row['links'] = ids.get(qid, 0)
        page = wp.get(qid, {})
        if page.get('extract'):
            row['about'] = page['extract'].strip()
            row['wiki'] = 'https://en.wikipedia.org/wiki/' + urllib.parse.quote((page.get('title') or wiki[qid]).replace(' ', '_'))
        elif qid in wiki:
            row['wiki'] = 'https://en.wikipedia.org/wiki/' + urllib.parse.quote(wiki[qid].replace(' ', '_'))
        name = images['want'].get(qid)
        meta = images['meta'].get(name or '')
        source = f'{cache}/img/{qid}.bin'
        if meta and os.path.exists(source) and meta.get('license'):
            target = os.path.join(out_dir, f'{qid}.webp')
            if not os.path.exists(target):
                subprocess.run(['convert', source + '[0]', '-background', 'white', '-alpha', 'remove', '-resize', '160x160>', '-quality', '78', target], check=False, capture_output=True)
            if os.path.exists(target):
                row['logo'] = {'file': f'images/world/{qid}.webp', 'source': meta['page'], 'credit': plain(meta.get('artist')) or 'Wikimedia Commons', 'license': meta['license'], 'licenseUrl': meta.get('licenseUrl')}
        result.append(row)
    result.sort(key=lambda r: (-r['links'], r['name']))
    # Descriptions load only when a festival is opened, which keeps the list and maps light.
    about = {row['id']: row.pop('about') for row in result if 'about' in row}
    with open(os.path.join(root, 'world-about.json'), 'w') as handle:
        json.dump(about, handle, ensure_ascii=False, separators=(',', ':'))
    with open(os.path.join(root, 'world-festivals.json'), 'w') as handle:
        json.dump({'source': 'Wikidata (CC0), English Wikipedia (CC BY-SA 4.0) and Wikimedia Commons', 'retrieved': time.strftime('%Y-%m-%d'), 'festivals': result}, handle, ensure_ascii=False, separators=(',', ':'))
    print(len(result), 'festivals,', sum('logo' in r for r in result), 'with images')


if __name__ == '__main__':
    {'fetch': fetch, 'build': build}[sys.argv[1]](sys.argv[2])
