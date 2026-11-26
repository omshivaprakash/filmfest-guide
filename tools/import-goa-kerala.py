"""Import Goa Panorama, Kerala screening schedules and documentary selections."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import unicodedata

import fitz
from lxml import html


IFFI = {
    2024: 'https://www.pib.gov.in/PressReleasePage.aspx?PRID=2067711&lang=2&reg=48',
    2025: 'https://www.pib.gov.in/PressReleasePage.aspx?PRID=2187868&lang=1&reg=3',
}
SCHEDULE = 'https://www.iffk.in/images/30th%20IFFK%20Screening%20Schedule.pdf'
IDS = 'https://idsffk.in/uploads/Downloads/Downloads1406202414%3A49%3A36.pdf'
KERALA_24 = 'https://www.fkha.in/assets/documents/magazine/December.pdf'
COMPETITION_24 = 'https://www.onmanorama.com/entertainment/entertainment-news/2024/12/12/iffk-2024-competition-films-when-where-to-watch-time-venue-full-list.html'


def panorama(path, year, add):
    source = IFFI[year]
    tables = html.parse(str(path)).xpath('//table[not(.//table)]')
    groups = []
    for table in tables:
        rows = [[' '.join(cell.text_content().split()) for cell in row.xpath('./td|./th')]
                for row in table.xpath('.//tr')]
        if len(rows) >= 5 and len(rows[0]) == 4 and rows not in groups:
            groups.append(rows)
    expected = [21, 6, 21] if year == 2024 else [6, 15, 6, 6, 11, 10]
    assert [len(rows) for rows in groups] == expected
    counts = Counter()
    for index, rows in enumerate(groups):
        is_non_feature = index >= (2 if year == 2024 else 4)
        format_name = 'Non-feature' if is_non_feature else 'Feature'
        section = 'Indian Panorama · Non-feature' if is_non_feature else 'Indian Panorama · Feature'
        if year == 2025 and index == 3:
            section = 'Indian Panorama · Debut Director nominees'
        for serial, title, language, director in rows:
            if 'title' in title.lower() and 'film' in title.lower() and 'director' in (language + director).lower():
                continue
            if year == 2025 and index == 3:
                language, director = director, language
            if title == 'GHAR JAISA KUCH':
                format_name = 'Short film'
            elif is_non_feature:
                format_name = 'Non-feature'
            counts[section] += 1
            add('iffi', year, title, format_name, language, 'India', director, source, section)
    assert counts['Indian Panorama · Feature'] == 25
    assert counts['Indian Panorama · Non-feature'] == 20


def documentary(folder, add):
    sections = [
        'Campus Films', 'Competition Long Documentary', 'Competition Short Documentary', 'Competition Short Documentary',
        'Competition Short Fiction', 'Competition Short Fiction', 'Focus Long Documentary', 'Focus Short Documentary',
        'Focus Short Documentary', 'Focus Short Fiction', 'Focus Short Fiction', 'Malayalam Long Documentary',
        'Malayalam Short Documentary', 'Malayalam Short Fiction', 'Music Video', 'Animation Films',
    ]
    for page, section in enumerate(sections, 1):
        text = (folder / f'page-{page:02}.txt').read_text()
        text = re.split(r'(?im)^.*idsffk\.in.*$', text)[0]
        format_name = ('Documentary' if 'Documentary' in section else 'Short film' if 'Fiction' in section
                       else 'Music video' if section == 'Music Video' else 'Format unlisted')
        entries = re.split(r'(?m)^\s*(?:\d{1,2}|[lI]{2})[.)]\s+', text)[1:]
        for entry in entries:
            if not re.search(r'\bDir[.:]\s*', entry, re.I):
                continue
            title, details = re.split(r'\bDir[.:]\s*', ' '.join(entry.split()), maxsplit=1, flags=re.I)
            director, _, language = re.sub(r'\s+\|\s+', ' / ', details).partition('/')
            title = title.split(' / ', 1)[0].replace(' | ', ' I ').strip()
            director = re.sub(r'\s+[*e]+(?:\s+e)*$', '', director).strip()
            language = re.sub(r'\s+e(?:\s+e)*$', '', language).strip()
            language = language.strip().strip('<>©*| ')
            if len(language) > 80:
                language = ''
            if title and len(director.strip()) <= 100:
                add('idsffk', 2024, title, format_name, language, '', director, f'{IDS}#page={page}', section)


def kerala_schedule(path, add):
    with fitz.open(path) as pdf:
        for page in pdf:
            spans = [span for block in page.get_text('dict')['blocks']
                     for line in block.get('lines', []) for span in line['spans']]
            for director in spans:
                if not director['text'].strip().startswith('Dir:'):
                    continue
                x, y = director['bbox'][:2]
                nearby = sorted((span for span in spans if abs(span['bbox'][0] - x) < 1.7
                                 and 0 < y - span['bbox'][1] < 74), key=lambda span: span['bbox'][1])
                title_parts = []
                metadata = []
                for span in nearby:
                    part = span['text'].strip()
                    if 'SemiBold' in span['font']:
                        if metadata:
                            title_parts, metadata = [], []
                        title_parts.append(part)
                    elif title_parts:
                        metadata.append(part)
                if not title_parts:
                    continue
                title = ' '.join(title_parts).split('/', 1)[0].strip().removeprefix('Opening Film ')
                meta = ' '.join(text for text in metadata if not re.fullmatch(r'\d+(?:/\d{4})?', text))
                country, _, language = meta.partition('/')
                if len(title) <= 100 and any(char.isalpha() for char in title):
                    add('iffk', 2025, title, 'Format unlisted', language, country,
                        director['text'].strip().removeprefix('Dir:'), f'{SCHEDULE}#page={page.number + 1}',
                        'Screening schedule')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('catalogue', type=Path)
    args = parser.parse_args()
    data = json.loads(args.catalogue.read_text())
    films = [film for film in data['films'] if not film.get('fromGoaKeralaImport')]

    def key(festival, year, title):
        normalized = unicodedata.normalize('NFKD', title.casefold())
        return festival, year, ''.join(char for char in normalized if char.isalnum())

    artwork = {key(film['festival'], film['year'], film['title']): film['artwork']
               for film in data['films'] if film.get('artwork')}
    seen = {key(film['festival'], film['year'], film['title']): film for film in films}
    added = Counter()

    def add(festival, year, title, format_name, language, country, director, source, section):
        title = title.strip()
        if not title or title == 'No Screening':
            return
        ref = key(festival, year, title)
        if ref in seen:
            film = seen[ref]
            if source not in film['sources']:
                film['sources'].append(source)
            film.setdefault('section', section)
            return
        credits = [['Director', name.strip()] for name in re.split(r',|\s+&\s+', director) if name.strip()]
        film = {'id': f'{festival}-{year}-programme-{added[festival, year] + 1}', 'title': title,
                'festival': festival, 'year': year, 'format': format_name, 'language': language.strip(),
                'country': country.strip(), 'section': section, 'summary': '', 'credits': credits,
                'awards': [], 'sources': [source], 'fromGoaKeralaImport': True}
        if ref in artwork:
            film['artwork'] = artwork[ref]
        seen[ref] = film
        films.append(film)
        added[festival, year] += 1

    for year in IFFI:
        panorama(args.input / f'iffi{year % 100}.html', year, add)
    documentary(args.input / 'ocr', add)
    kerala_schedule(args.input / 'iffk25.pdf', add)
    records = Path(__file__).with_name('iffk-2024-selections.tsv').read_text().splitlines()
    for line in records:
        section, title, language, country, director = line.split('\t')
        add('iffk', 2024, title, 'Format unlisted', language, country, director,
            COMPETITION_24 if section == 'International Competition' else KERALA_24, section)
    editions = [
        ('iffi', 2024, '55th', '20–28 November', IFFI[2024], 'Indian Panorama selection'),
        ('iffi', 2025, '56th', '20–28 November', IFFI[2025], 'Indian Panorama selection'),
        ('iffk', 2024, '29th', '13–20 December', COMPETITION_24, 'Competition screenings'),
        ('iffk', 2025, '30th', '12–19 December', SCHEDULE, 'Screening schedule PDF'),
        ('idsffk', 2024, '16th', '26–31 July', IDS, 'Official selection PDF'),
    ]
    for festival_id, year, number, dates, url, label in editions:
        festival = next(festival for festival in data['festivals'] if festival['id'] == festival_id)
        edition = next((record for record in festival['editions'] if record['year'] == year), None)
        if edition is None:
            edition = {'year': year, 'number': number, 'dates': dates, 'source': url}
            festival['editions'].append(edition)
        edition.update(catalogue=url, catalogueLabel=label)
        festival['editions'].sort(key=lambda record: record['year'], reverse=True)
    goa_awards = 'https://www.pib.gov.in/PressReleasePage.aspx?PRID=2196146&lang=2&reg=48'
    kerala_awards = 'https://iffk.in/articledetview/MTczMzU3MzIuOTI%3D'
    ids_awards = 'https://www.newindianexpress.com/amp/story/cities/thiruvananthapuram/2024/Aug/01/anand-patwardhan-wins-best-long-documentary-award-at-idsffk'
    for title, director, country in [
        ('Skin of Youth', 'Ashleigh Mayfair', 'Vietnam'),
        ('My Daughter’s Hair', 'Hesam Farahmand', 'Iran'),
        ('Fränk', 'Tõnis Pill', 'Estonia'),
        ('Safe House', 'Eirik Svensson', 'Norway'),
    ]:
        add('iffi', 2025, title, 'Feature', '', country, director, goa_awards, 'Festival award winner')
    for festival, year, title, name, url, recipient in [
        ('iffi', 2025, 'Skin of Youth', 'Golden Peacock · Best Film', goa_awards, ''),
        ('iffi', 2025, 'Gondhal', 'Silver Peacock · Best Director', goa_awards, 'Santosh Davakhar'),
        ('iffi', 2025, 'My Daughter’s Hair', 'Best Debut Feature Film of a Director (joint)', goa_awards, 'Hesam Farahmand'),
        ('iffi', 2025, 'Fränk', 'Best Debut Feature Film of a Director (joint)', goa_awards, 'Tõnis Pill'),
        ('iffi', 2025, 'Safe House', 'ICFT–UNESCO Gandhi Medal', goa_awards, ''),
        ('iffk', 2025, 'Two Seasons, Two Strangers', 'Golden Crow Pheasant · Best Film', kerala_awards, ''),
        ('idsffk', 2024, 'Dolls Don’t Die', 'Second Best Long Documentary', ids_awards, 'Ranajit Ray'),
        ('idsffk', 2024, 'Farming The Revolution', 'Special Jury Award · Long Documentary', ids_awards, ''),
    ]:
        film = seen[key(festival, year, title)]
        award = [name, url] + ([recipient] if recipient else [])
        if award not in film['awards']:
            film['awards'].append(award)
    honor = {'festival': 'iffi', 'year': 2025, 'role': 'Actor',
             'award': ['Honour for 50 years in cinema',
                       'https://www.pib.gov.in/PressReleasePage.aspx?PRID=2196172&lang=2&reg=48', 'Rajinikanth']}
    if honor not in data['honors']:
        data['honors'].append(honor)
    data['films'] = films
    args.catalogue.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    for edition, count in sorted(added.items()):
        print(*edition, count)


if __name__ == '__main__':
    main()
