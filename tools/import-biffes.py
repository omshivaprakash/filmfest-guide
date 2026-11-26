"""Import title/page entries from BIFFes catalogue text (pdftotext -layout)."""
import argparse
import json
from pathlib import Path
import re
import unicodedata

EDITIONS = [2006, 2008, 2009, 2011, 2012, 2013, 2014, 2016, 2017,
            2018, 2019, 2020, 2022, 2023, 2024, 2025, 2026]
INDEX = re.compile(r'^\s*(?:index(?: of films)?|films? i\s*n\s*d\s*e\s*x|movie index)\s*$', re.I)
ENTRY = re.compile(r'\s*(\S.*?)\s{2,}(\d{1,3}(?:,\s*\d{1,3})*)(?=\s|$)')
META = re.compile(r'^\s*(\d{4})\s*/\s*([^/]+?)\s*/\s*([^/]+?)\s*/\s*(\d+)\s*min(?:s|utes)?\.?\s*/\s*(.+?)\s*$', re.I)


def normalized(title):
    return ''.join(char for char in unicodedata.normalize('NFKD', title.casefold()) if char.isalnum())


def indexed_titles(pages):
    entries = []
    for page_index, page in enumerate(pages):
        if not any(INDEX.fullmatch(line) for line in page.splitlines()):
            continue
        for index_page in pages[page_index:page_index + 6]:
            rows = []
            for line in index_page.splitlines():
                line = line.replace('\b', '\t').expandtabs(4)
                for match in ENTRY.finditer(line):
                    title, page_no = match.groups()
                    if any(char.isalnum() for char in title) and not re.search(r'\s{3,}', title):
                        if not INDEX.fullmatch(title) and not re.search(r'Bengaluru International Film Festival$', title, re.I):
                            rows.append((title.strip(), int(page_no.split(',')[0])))
            if len(rows) < 8:
                break
            entries.extend(rows)
        if entries:
            break
    return entries


def metadata_titles(pages):
    entries = []
    header = re.compile(r'^\s*(\d{4})\s*/\s*([^/]+?)\s*/\s*([^/]+?)\s*/')
    credit_labels = {
        'Producer': 'Producer', 'Editor': 'Editor', 'Writer': 'Writer',
        'Screenplay': 'Writer', 'DOP': 'Cinematographer', 'Sound': 'Sound',
        'Music': 'Composer', 'Cast': 'Actor',
    }
    for page_index, page in enumerate(pages, 1):
        lines = [line.strip() for line in page.splitlines() if line.strip()]
        for position, line in enumerate(lines[:10]):
            match = header.match(line)
            if not match:
                continue
            _, country, language = match.groups()
            full = META.fullmatch(line)
            if position and full:
                title = lines[position - 1]
                director = full.group(5)
            elif position == 0 and len(lines) > 1:
                title = re.split(r'\s{2,}', lines[1])[0]
                if not any(ch.isascii() and ch.isalpha() for ch in title) or re.match(r'^\d+\s*min', title, re.I):
                    continue
                director = ''
            else:
                continue
            credit_lines = [re.split(r'\s{2,}', line)[0] for line in lines[:36]]
            if not director:
                director = next((line.partition(':')[2].strip() for line in credit_lines if line.startswith('Director:')), '')
            credits = [('Director', name.strip()) for name in director.split(',') if name.strip()]
            for line in credit_lines:
                label, _, names = line.partition(':')
                if label in credit_labels:
                    credits.extend((credit_labels[label], name.strip()) for name in names.split(',')
                                   if name.strip() and not re.search(r'\b(?:productions?|pictures|studios?|films|entertainment)\b', name, re.I))
            entries.append((title, page_index, country, language, list(dict.fromkeys(credits))))
            break
    return entries


def modern_credits(pages):
    header = re.compile(r'^DIRECTOR\s*[-:–]\s*(.+?)\s{2,}([^/]+?)\s*/\s*\d{4}\s*/\s*([^/]+?)\s*/', re.I)
    labels = {'producer': 'Producer', 'screenplay': 'Writer', 'dop': 'Cinematographer', 'editor': 'Editor',
              'sound': 'Sound', 'music': 'Composer', 'cast': 'Actor'}
    details = {}
    for page_no, page in enumerate(pages, 1):
        lines = [line.replace('\b', ' ').strip() for line in page.splitlines() if line.strip()]
        if not lines:
            continue
        match = next((header.match(line) for line in lines[:6] if header.match(line)), None)
        if not match:
            continue
        title = re.split(r'\s{3,}', lines[0])[0]
        director, country, language = match.groups()
        credits = [('Director', re.split(r'\s{3,}', name.strip())[0].title()) for name in director.split(',') if name.strip()]
        for line in lines[6:]:
            for column in re.split(r'\s{3,}', line):
                credit = re.fullmatch(r'(Producer|Screenplay|DOP|Editor|Sound|Music|Cast)\s*:\s*(.+)', column, re.I)
                if credit:
                    role, names = credit.groups()
                    credits.extend((labels[role.lower()], name.strip()) for name in names.split(',')
                                   if name.strip() and len(name.strip()) <= 55 and '|' not in name
                                   and not re.search(r'\b(?:productions?|pictures|studios?|films|entertainment)\b', name, re.I))
        details[normalized(title)] = (page_no, country.strip().title(), language.strip().title(), list(dict.fromkeys(credits)))
    return details


def archived_2011(path):
    source = 'https://archive.org/download/unset0000unse_n1n9/unset0000unse_n1n9.pdf'
    text = path.read_text(errors='replace')
    pattern = re.compile(r'^([^\n]+?)\s*\(\s*(?:19|20)\d{2}\s*\|\s*\d{1,3}\s*min\b([^)]{0,180})\)', re.M | re.I)
    entries = []
    for match in pattern.finditer(text):
        title, details = match.groups()
        title = title.strip()
        if title.startswith('('):
            previous = text[:match.start()].rstrip().rsplit('\n', 1)[-1].strip()
            title = f'{previous} {title}'
        parts = [' '.join(part.split()) for part in details.strip('| ').split('|')]
        if len(parts) != 4 or not parts[-1].upper().startswith('DIR:'):
            continue
        if not title[0].isalnum() or not title.isupper() or not any(ch.isalpha() for ch in title):
            continue
        _, country, language, director = parts
        director = director.partition(':')[2].strip()
        if not director or not all(ch.isalpha() or ch in " .’'-," for ch in director):
            continue
        credits = [('Director', name.strip()) for name in director.split(',') if name.strip()]
        entries.append((title, None, country, language, credits))
    return source, entries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    catalog = json.loads(args.output.read_text())
    sources = json.loads(Path(__file__).with_name('biffes-sources.json').read_text())
    festival = next(entry for entry in catalog['festivals'] if entry['id'] == 'biffes')
    editions = {record['year']: record for record in festival['editions']}
    artwork = {(film['year'], normalized(film['title'])): film['artwork']
               for film in catalog['films'] if film['festival'] == 'biffes' and film.get('artwork')}
    original = [film for film in catalog['films'] if not film.get('fromCatalogue')]
    known = {(film['year'], normalized(film['title'])): film for film in original if film['festival'] == 'biffes'}
    imported = []
    for number, year in enumerate(EDITIONS, 1):
        source = sources[str(number)]
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number, 'th')
        edition = editions.setdefault(year, {'year': year, 'number': f'{number}{suffix}', 'dates': ''})
        edition.update(catalogue=source)
        if year == 2026:
            edition['dates'] = '29 January–6 February'
        edition.setdefault('source', source)
        path = args.input / f'{number}.txt'
        if number == 9 and (not path.exists() or path.stat().st_size < 10000):
            path = args.input / '9-ocr.txt'
        edition['importedTitles'] = 0
        if not path.exists():
            continue
        pages = path.read_text(errors='replace').split('\f')
        if number == 9 and path.name == '9-ocr.txt':
            source = 'https://archive.org/download/biffes.9th-biffes-catalogue-2017/9th-BIFFES-Catalogue-2017_text.pdf'
        if number == 4 and (args.input / '4-ocr.txt').exists():
            source, entries = archived_2011(args.input / '4-ocr.txt')
        else:
            entries = metadata_titles(pages) if number == 14 else indexed_titles(pages)
        print(f'{year}: {len(entries)} extracted entries')
        if number in (15, 16, 17):
            details = modern_credits(pages)
            entries = [(title, *details[normalized(title)]) if normalized(title) in details else (title, page)
                       for title, page in entries if title != 'IN COLLABORATION WITH']
        for title, page, *metadata in entries:
            key = (year, normalized(title))
            if not key[1]:
                continue
            if key in known:
                film = known[key]
                if source not in film['sources']:
                    film['sources'].append(source)
                continue
            country, language, credits = metadata or ('', '', [])
            record = {
                'id': f'biffes-{year}-{len(imported) + 1}', 'title': title, 'festival': 'biffes',
                'year': year, 'format': 'Format unlisted', 'language': language, 'country': country,
                'summary': '', 'credits': credits, 'awards': [],
                'sources': [f'{source}#page={page}' if metadata and page else source],
                **({'cataloguePage': page} if page and not metadata else {}), 'fromCatalogue': True,
            }
            if key in artwork:
                record['artwork'] = artwork[key]
            known[key] = record
            imported.append(record)
        edition['importedTitles'] = sum(record['year'] == year for record in imported)
    imported.sort(key=lambda record: (-record['year'], record['title'].casefold()))
    festival['editions'] = sorted(editions.values(), key=lambda item: item['year'], reverse=True)
    catalog['films'] = original + imported
    args.output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
