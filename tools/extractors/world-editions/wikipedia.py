"""Read selections and award lists from English Wikipedia edition articles ("78th Locarno Film Festival").

Only facts are kept (title, director, country, section, award); each record links the article it came from.
"""
import json, re, sys, time, urllib.parse, urllib.request

API = 'https://en.wikipedia.org/w/api.php'
UA = {'User-Agent': 'filmfest-guide-data/1.0 (open data project; github.com/omshivaprakash/filmfest-guide)'}
SKIP_SECTION = re.compile(r'jur|industry|academy|residen|lab\b|market|tutor|reference|external|see also|note|programm(er|ing team)', re.I)
AWARD_SECTION = re.compile(r'award|prize|winner|palmar', re.I)


def fetch_pages(urls):
    """Map each https://en.wikipedia.org/wiki/<title> URL to its wikitext, 20 titles a request."""
    titles = {urllib.parse.unquote(u.rsplit('/wiki/', 1)[1]).replace('_', ' '): u for u in urls}
    pages, keys = {}, sorted(titles)
    for i in range(0, len(keys), 20):
        query = urllib.parse.urlencode({'action': 'query', 'prop': 'revisions', 'rvprop': 'content', 'rvslots': 'main', 'redirects': 1,
                                        'format': 'json', 'formatversion': 2, 'titles': '|'.join(keys[i:i + 20])})
        for attempt in range(5):
            try:
                data = json.load(urllib.request.urlopen(urllib.request.Request(f'{API}?{query}', headers=UA), timeout=120))
                break
            except Exception as error:
                print('retry', attempt + 1, error, file=sys.stderr)
                time.sleep(int(getattr(error, 'headers', {}).get('Retry-After') or 0) or 15 * (attempt + 1))
        else:
            raise SystemExit('Wikipedia request failed; keeping the existing shard')
        moved = {r['to']: r['from'] for r in data['query'].get('redirects', [])}
        moved.update({n['to']: n['from'] for n in data['query'].get('normalized', [])})
        for page in data['query']['pages']:
            if 'revisions' in page:
                title = page['title']
                while title not in titles and title in moved:
                    title = moved[title]
                if title in titles:
                    pages[titles[title]] = page['revisions'][0]['slots']['main']['content']
        time.sleep(3)  # Wikimedia asks bots to go slowly
    return pages


def link_target(text):
    m = re.search(r'\[\[([^\]|#]+)', text)
    return 'https://en.wikipedia.org/wiki/' + urllib.parse.quote(m.group(1).strip().replace(' ', '_')) if m else None


def clean(text):
    text = re.sub(r'<small>.*?</small>|<sup.*?</sup>|<br\s*/?>', ' ', text, flags=re.S | re.I)
    text = re.sub(r'\{\{(?:flag|flagcountry|flagu)\|([^|}]+)[^}]*\}\}', r'\1', text, flags=re.I)
    text = re.sub(r'\{\{(?:lang|langx)\|[^|}]+\|([^|}]+)[^}]*\}\}', r'\1', text, flags=re.I)
    text = re.sub(r'\{\{(?:nowrap|ill|interlanguage link|sortname|sort)\|([^|}]+)(?:\|([^|}]+))?[^}]*\}\}',
                  lambda m: f'{m.group(1)} {m.group(2)}' if m.group(0).lower().startswith('{{sortname') and m.group(2) else m.group(1), text, flags=re.I)
    text = re.sub(r'\{\{[^{}]*\}\}', '', text)
    text = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]', r'\1', text)
    text = re.sub(r"'{2,}|<[^>]+>|&nbsp;", ' ', text)
    return re.sub(r'\s+', ' ', text).strip(' ,;:–-|')


def strip_noise(wikitext):
    return re.sub(r'<ref[^>]*/>|<ref.*?</ref>|<!--.*?-->', '', wikitext, flags=re.S)


def cells(line):
    """Split a table row line into cells, expanding colspan and dropping attributes."""
    out = []
    for cell in re.split(r'\|\||!!', line.lstrip('|!')):
        span = re.match(r'\s*[^|\[\]]*colspan\s*=\s*"?(\d+)"?[^|\[\]]*\|(?!\|)', cell)
        attr = re.match(r'\s*(?:scope|style|class|rowspan|colspan|align|width|data-sort-value)[^|\[\]]*\|(?!\|)', cell)
        if attr:
            cell = cell[attr.end():]
        out += [cell] * (int(span.group(1)) if span else 1)
    return out


def read_table(lines, i):
    """Read the wikitable starting at lines[i]; return (index of its closing line, lowercased header, rows of raw cells)."""
    header, rows, row, body = [], [], [], False
    i += 1
    while i < len(lines) and not lines[i].strip().startswith('|}'):
        cell = lines[i].strip()
        if cell.startswith('|-'):
            if row:
                rows.append(row)
            row, body = [], bool(header)
        elif cell.startswith('!') and not body:
            header += [clean(c).lower() for c in cells(cell)]
        elif cell.startswith(('|', '!')) and not cell.startswith('|+'):  # "! 1946" is a row header cell
            row += cells(cell)
        elif row:
            row[-1] += ' ' + cell
        i += 1
    if row:
        rows.append(row)
    return i, header, rows


def column(header):
    return lambda *words: next((n for n, h in enumerate(header) if any(w in h for w in words)), None)


def award_title(heading):
    return re.sub(r'^(?:list of\s+)?(?:winners of\s+(?:the\s+)?)?|\s+(?:winners|recipients|laureates)$', '', heading, flags=re.I).strip()


def winners(wikitext, award=None):
    """Year-by-year winner tables: [(award, year, title, link, director, country)].

    In a festival's main article only award sections count and the award is the section heading; in an award's
    own article (award given) every table counts. A table where a year repeats lists nominees, so it is skipped.
    """
    text = strip_noise(wikitext)
    lines, heads, out, i = text.split('\n'), {}, [], 0
    while i < len(lines):
        line = lines[i].strip()
        head = re.match(r'^(=+)\s*(.*?)\s*\1$', line)
        if head:
            heads = {k: v for k, v in heads.items() if k < len(head.group(1))}
            heads[len(head.group(1))] = clean(head.group(2))
        path = ' / '.join(heads[k] for k in sorted(heads))
        if line.startswith('{|') and not SKIP_SECTION.search(path):
            start = i
            i, header, rows = read_table(lines, i)
            col = column(header)
            y, t, d, c = col('year'), col('english title', 'title', 'film'), col('director'), col('countr')
            # outside award sections, a film column headed like "Best Film (Étoile d'Or Winner)" names its award
            named = t is not None and 'winner' in header[t] and re.search(r'\(([^()]+?)\s+winners?\)', '\n'.join(lines[start:i]), re.I)
            name = award or (award_title(heads[max(heads)] if heads else '') if AWARD_SECTION.search(path) else clean(named.group(1)) if named else None)
            found = []
            for r in rows if None not in (y, t, d) and name else []:
                if len(r) < len(header):  # a rowspan row: several films share a year
                    found = []
                    break
                year = re.search(r'\b(19[3-9]\d|20\d\d)\b', clean(r[y]))
                if year and "''" in r[t] and clean(r[t]):  # winners are italicised; "Not held" rows are not
                    found.append((name, int(year.group(1)), clean(r[t]), link_target(r[t]),
                                  clean(r[d]), clean(r[c]).strip('* ') if c is not None else ''))
            if len({f[1] for f in found}) == len(found):
                out += found
        i += 1
    return out


def parse(wikitext):
    """Return (selections, awards): [(section, title, link, director, country)], [(award, title, link)]."""
    text = strip_noise(wikitext)
    selections, awards, heads = [], [], {}
    lines, i = text.split('\n'), 0
    award_name = None
    while i < len(lines):
        line = lines[i].strip()
        head = re.match(r'^(=+)\s*(.*?)\s*\1$', line)
        if head:
            heads = {k: v for k, v in heads.items() if k < len(head.group(1))}
            heads[len(head.group(1))] = clean(head.group(2))
            award_name = None
        path = ' / '.join(heads[k] for k in sorted(heads))
        if line.startswith('{|') and not SKIP_SECTION.search(path):
            i, header, rows = read_table(lines, i)
            col = column(header)
            t, d, c = col('english title', 'title', 'film'), col('director'), col('countr')
            if t is not None and d is not None:
                section = heads.get(3) or heads.get(2) or ''
                for r in rows:  # a short row sits under a rowspan, so its cells are shifted: skip it
                    # a colspan row repeats one label across title and director: it is a section heading, not a film
                    if len(r) >= len(header) and clean(r[t]) and clean(r[t]) != clean(r[d]) and not re.fullmatch(r'[\d\s–-]*', clean(r[d])):
                        selections.append((section, clean(r[t]), link_target(r[t]), clean(r[d]), clean(r[c]) if c is not None and c < len(r) else ''))
        elif line.startswith('*') and AWARD_SECTION.search(path) and not SKIP_SECTION.search(path):
            depth, body = len(line) - len(line.lstrip('*')), line.lstrip('*').strip()
            name, _, rest = body.partition(':') if ':' in body and not body.startswith("''") else ('', '', body)
            if depth == 1 and name:
                award_name = clean(name)
            seg = re.sub(r"(?<!')'''(?!')(.*?)(?<!')'''(?!')", r'\1', rest if name else body)  # bold marks award names, not films
            title = re.search(r"''+(.+?)''+", seg)
            winner = award_name if depth > 1 or not name else clean(name)
            if title and winner:  # "''Film'' by X" and "Person for ''Film''" both credit the film
                awards.append((winner, clean(title.group(1)), link_target(title.group(1))))
        i += 1
    return selections, awards


def check():
    sample = """== Official sections ==
=== Main Competition ===
{| class="wikitable"
!scope="col"| English Title
!scope="col"| Original Title
!scope="col"| Director(s)
!scope="col"| Production Country
|-
| colspan=2|''[[The Birthday Party (2025 film)|The Birthday Party]]''
| Miguel Ángel Jiménez
| Greece, Spain
|-
! colspan=4 | Special Screenings
|-
| ''[[Heads or Tails? (2025 film)|Heads or Tails?]]''
| ''Testa O Croce?''
| [[Alessio Rigo de Righi]] and Matteo Zoppis<ref>x</ref>
| {{flag|Italy}}
|}
== Juries ==
{| class="wikitable"
!Name !! Director
|-
| A || B
|}
== Official Awards ==
* [[Golden Leopard]]: ''[[Two Seasons, Two Strangers]]'' by Sho Miyake
* [[Best Performance Award (Locarno)|Pardo for Best Performance]]:
** Marya Imbro for ''[[White Snail]]''
"""
    table = """== Golden Prize winners ==
{| class="wikitable"
! Year !! Film !! Director !! Country
|-
| 1967 || colspan="3"| Festival not held
|-
| 1968 || ''[[Bonnie and Clyde (film)|Bonnie and Clyde]]'' || [[Arthur Penn]] || {{USA}}*
|}
== Programme ==
{| class="wikitable"
! Year !! Film !! Director
|-
| 1968 || ''Opening Film'' || X
|}
"""
    assert winners(table) == [('Golden Prize', 1968, 'Bonnie and Clyde', 'https://en.wikipedia.org/wiki/Bonnie_and_Clyde_%28film%29', 'Arthur Penn', '')], winners(table)
    nominees = table.replace('| 1967 || colspan="3"| Festival not held', "| 1968 || ''Other'' || Y || Z")
    assert winners(nominees) == [] and len(winners(table.split('== Programme')[0].replace('Golden Prize winners', 'History'), 'Big Award')) == 1
    ceremonies = "== Ceremonies ==\n{|\n! Edition\n! Year\n! Best Film (Étoile d'Or Winner)\n! Director\n|-\n| 1st\n| 2001\n| ''[[Inch'Allah Dimanche]]''\n| Yamina Benguigui\n|}"
    assert [w[:3] for w in winners(ceremonies)] == [("Étoile d'Or", 2001, "Inch'Allah Dimanche")], winners(ceremonies)
    assert winners(ceremonies.replace(" (Étoile d'Or Winner)", '')) == []  # a plain film table outside award sections is not a winner list
    sel, aw = parse(sample)
    assert sel == [('Main Competition', 'The Birthday Party', 'https://en.wikipedia.org/wiki/The_Birthday_Party_%282025_film%29', 'Miguel Ángel Jiménez', 'Greece, Spain'),
                   ('Main Competition', 'Heads or Tails?', 'https://en.wikipedia.org/wiki/Heads_or_Tails%3F_%282025_film%29', 'Alessio Rigo de Righi and Matteo Zoppis', 'Italy')], sel
    assert aw == [('Golden Leopard', 'Two Seasons, Two Strangers', 'https://en.wikipedia.org/wiki/Two_Seasons%2C_Two_Strangers'),
                  ('Pardo for Best Performance', 'White Snail', 'https://en.wikipedia.org/wiki/White_Snail')], aw
