"""Add Bengaluru award results and programme titles from Servants of Knowledge."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import unicodedata

import fitz

BASE = 'https://archive.org/details/'
AWARDS = 'biffes.12th-biffes-award-winners-awards-2020'
DOCUMENTS = {
    2011: [('Film catalogue', 'unset0000unse_n1n9')],
    2013: [('Film catalogue', 'biffes.6th-biffes-festival-2013'), ('Alternate scan', 'unset0000unse_o1g5')],
    2014: [('Film catalogue', 'biffes.7th-biffes-film-festival-2014'),
           ('Screening schedule', 'bengaluru-international-film-festival-7th-biffes-2014-catalog')],
    2016: [('Film catalogue', 'biffes.8th-biffes-2016'), ('Alternate scan', 'unset0000unse_o4g5')],
    2017: [('Film catalogue', 'biffes.9th-biffes-catalogue-2017')],
    2018: [('Film catalogue', 'biffes.10th-biffes-catalog')],
    2019: [('Film catalogue', 'biffes.11-biffes-19-catalog')],
    2020: [('Film catalogue', 'biffes.12th-biffes-films-catalogue'), ('Alternate scan', 'catalogue-12biffes-2020'),
           ('Screening schedule', '12th-biffes-schedule-v-02')],
    2022: [('Screening schedule', 'biffes.13th-biffes-screening-schedule-final')],
    2023: [('Screening schedule', 'biffes.14th-biffes-screening-schedule-2023')],
}
DATES = {2011: '15–22 December', 2012: '20–27 December', 2013: '26 December–2 January',
         2014: '4–11 December', 2016: '28 January–4 February', 2017: '2–9 February',
         2018: '22 February–1 March', 2019: '21–28 February', 2020: '26 February–4 March'}
# The first three pages cover the 12th edition. Later pages in the same item
# reproduce awards from the 11th through the 4th edition.
AWARD_YEARS = [2020, 2019, 2018, 2017, 2016, 2014, 2013, 2012, 2011]


def key(value):
    return ''.join(char for char in unicodedata.normalize('NFKD', value.casefold()) if char.isalnum())


def schedule(path):
    with fitz.open(path) as pdf:
        for page in pdf:
            spans = [(i, s) for i, b in enumerate(page.get_text('dict')['blocks'])
                     for line in b.get('lines', []) for s in line['spans']]
            for block, director in spans:
                match = re.match(r'^\s*Dir:\s*(\S.*)$', director['text'])
                if not match:
                    continue
                left, top, right, _ = director['bbox']
                center = (left + right) / 2
                candidates = {}
                for nearby_block, span in spans:
                    x0, y0, x1, y1 = span['bbox']
                    text = span['text'].strip()
                    if (-1.6 < top - y1 < 24 and abs((x0 + x1) / 2 - center) < 14
                            and span['size'] > director['size'] + .5 and abs(block - nearby_block) <= 3
                            and not re.search(r'\b(?:Hrs|mins|AM|PM)\b', text, re.I)
                            and re.search(r'[A-Za-z]{2}', text)):
                        row = round(y0)
                        score = abs(block - nearby_block)
                        if row not in candidates or score < candidates[row][0]:
                            candidates[row] = (score, text)
                if not candidates:
                    continue
                title = ' '.join(dict.fromkeys(candidates[row][1] for row in sorted(candidates)))
                if len(title) > 110 or re.search(r'\b(?:DIRECTOR|SCREENINGS|NO SHOW|CINEMA COMPETITION)\b', title, re.I):
                    continue
                yield title, match.group(1).strip(), page.number + 1


def awards(path):
    year = None
    section = ''
    award = ''
    for page_no, page in enumerate(path.read_text().split('\f'), 1):
        lines = [' '.join(line.replace('\uf020', '').split()) for line in page.splitlines()]
        lines = [line for line in lines if line]
        for i, line in enumerate(lines):
            header = re.match(r'^(\d+)(?:th|rd|nd|st) BIFFes Award Winners', line)
            if header:
                year = AWARD_YEARS[12 - int(header.group(1))]
                section = award = ''
                continue
            if re.match(r'^(ASIAN|INDIAN|KANNADA) CINEMA COMPETITION$|^Kannada Cinema Popular Entertainment$', line):
                section = line.title()
                award = ''
                continue
            if not line.startswith(''):
                if re.match(r'^(?:BEST|MOST POPULAR|SPECIAL|JURY|THE SPECIAL|THE NETPAC|NETPAC|FIPRESCI|FIRST|SECOND|THIRD|2nd|3rd|CHITRABHARATI|KANNADA CINEMA|ASIAN CINEMA AWARD|INDIAN CINEMA AWARD)', line, re.I):
                    award = line
                    if re.search(r'^Kannada Cinema Competition Confers.*Best Kannada', line, re.I):
                        award = 'Best Kannada Film'
                    elif re.search(r'^Kannada Cinema Competition Confers.*Special Jury', line, re.I):
                        award = 'Special Jury Award · Kannada Cinema'
                    elif re.search(r'^Chitrabharati.*Suchitra Samman', line, re.I):
                        award = 'Suchitra Samman · Best Indian Film'
                    elif re.search(r'^Chitrabharati.*Special Jury', line, re.I):
                        award = 'Special Jury Award · Indian Cinema'
                continue
            title = line.removeprefix('').strip()
            tail = lines[i + 1:i + 2]
            if title.count('(') > title.count(')') and tail:
                title = f'{title} {tail[0]}'
                tail = lines[i + 2:i + 3]
            director = producer = ''
            if tail:
                match = re.match(r'(?:(?:Produced & )?Directed(?: & Produced)? by|Director:)\s*[–-]?\s*(.+?)(?:\s+(?:and |& )?Produc(?:ed by|er:?)|\s*\|\s*Producer:|$)', tail[0], re.I)
                if match:
                    director = match.group(1).strip().strip(',').strip()
                credit = re.search(r'\b(?:Produced by|Producer:)\s*[–-]?\s*(.+)$', tail[0], re.I)
                if credit:
                    producer = credit.group(1).strip().strip(',').strip()
                elif re.match(r'Produced & Directed by|Directed & Produced by', tail[0], re.I):
                    producer = director
            title = re.split(r'\s+[–-]\s+', title, 1)[0]
            title = re.sub(r'\s*\([^)]*(?:Language|Film|South Korea|Kyrgyzstan|South Africa|Marathi)\)$', '', title, flags=re.I)
            title = {'LUKY': 'Lucky', 'N0.89 SHIMEN ROAD': 'No. 89 Shimen Road', 'HAPPY OLD YEAR': 'Happy Old Year'}.get(title, title)
            clean_award = award.title() if award.isupper() else award
            clean_award = re.sub(r'\b(Netpac|Fipresci)\b', lambda m: m.group().upper(), clean_award, flags=re.I)
            if section and not re.search(r'NETPAC|FIPRESCI', clean_award, re.I):
                clean_award += ' · ' + section
            if year and clean_award and title:
                yield year, title, director, producer, clean_award, page_no


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('catalogue', type=Path)
    args = parser.parse_args()
    data = json.loads(args.catalogue.read_text())
    bi = next(festival for festival in data['festivals'] if festival['id'] == 'biffes')
    editions = {edition['year']: edition for edition in bi['editions']}
    films = data['films']
    by_title = {}
    added = Counter()

    def aliases(title):
        short = title.split('(', 1)[0].strip(' "')
        variants = [title, short, *re.findall(r'\(([^)]+)\)', title), *re.split(r'\s+[/|]\s+', short)]
        return {key(part) for variant in variants for part in [variant, re.sub(r'^the\s+', '', variant, flags=re.I)] if key(part)}

    def index(film):
        for alias in aliases(film['title']):
            by_title.setdefault((film['year'], alias), {})[film['id']] = film

    for film in films:
        if film['festival'] == 'biffes':
            index(film)

    def merge(year, title, director, source, kind):
        matches = {ident: film for alias in aliases(title) for ident, film in by_title.get((year, alias), {}).items()}
        if len(matches) > 1:
            return None
        if matches:
            film = next(iter(matches.values()))
        else:
            film = {'id': f'biffes-sok-{year}-{key(title)}', 'title': title, 'festival': 'biffes', 'year': year,
                    'format': 'Format unlisted', 'language': '', 'country': '', 'summary': '',
                    'credits': [], 'awards': [], 'sources': [], 'section': kind}
            films.append(film)
            index(film)
            added[year] += 1
        if source and source not in film['sources']:
            film['sources'].append(source)
        if director and not any(role == 'Director' for role, _ in film['credits']):
            film['credits'].extend(['Director', name.strip()] for name in re.split(r',|\s+[&|]\s+', director) if name.strip())
        return film

    for year in (2022, 2023):
        item_id = DOCUMENTS[year][0][1]
        for title, director, page in schedule(args.input / f'schedule{year}.pdf'):
            if title in {'BAD LUCK BANGING', 'NO GROUND BENEATH THE FEE', 'IT’S A RESURRECTION', 'SATYAJIT RAY'}:
                continue
            title = {
                '180 DEGREE RULE': '180°Rule',
                'WHEEL OF FORTUNE & FANTASY': 'Wheel of Fortune and Fantasy',
                'SAUDI VELLAKKA CC NO 225/2009': 'Saudi Vellakka',
                'THE MONK & THE COURTESAN': 'The Monk and the Courtesan',
                'A HOUSE WITH NO NAME': 'A House with No Names',
            }.get(title, title)
            merge(year, title, director, f'{BASE}{item_id}/page/n{page-1}', 'Screening schedule')

    count = 0
    for year, title, director, producer, name, page in awards(args.input / 'awards2020.txt'):
        title = {'Happy Old Year': 'Happy Old Years', 'KAVALUDARI': 'Kavaludaari',
                 'PRAKRUTI': 'Prakruthi'}.get(title, title)
        source = f'{BASE}{AWARDS}/page/n{page-1}'
        film = merge(year, title, director, source, 'Festival award winner')
        award = [name, source]
        if film and producer and not any(role == 'Producer' for role, _ in film['credits']):
            for candidate in re.split(r',|\s+(?:&|and)\s+', producer):
                candidate = candidate.strip()
                if candidate and not re.search(r'\b(?:Studio|Creations|Limited|Cinema|Productions?|Pictures|Films?|Entertainment|Media|NFDC|Info)\b|\bUAN\b|/', candidate, re.I):
                    film['credits'].append(['Producer', candidate])
        if film and award not in film['awards']:
            film['awards'].append(award)
            count += 1

    for year, edition in editions.items():
        documents = list(DOCUMENTS.get(year, []))
        if year in AWARD_YEARS:
            documents.append(('Award winners, 2011–2020', AWARDS))
            edition['dates'] = DATES[year]
        if documents:
            edition['archiveDocuments'] = [{'name': name, 'url': BASE + ident} for name, ident in documents]

    args.catalogue.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print('New films:', dict(sorted(added.items())))
    print('Awards added:', count)


if __name__ == '__main__':
    main()
