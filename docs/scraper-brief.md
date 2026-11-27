# Scraper brief: data still to pull

What the guide is missing, ranked by how much a visitor would notice, and the exact file shape each scraper should write so its output drops straight in. Audited against `main` on 2026-11-27 (after the Marrakech and India merges): 57 guide festivals, 48,729 films, 1,498 honours, 8,128 world festivals.

Field meanings are in the [data dictionary](DATA-DICTIONARY.md). Every rule below comes from `check-catalog.mjs`; run `node check-catalog.mjs` after dropping a file in, and it will name the record that breaks.

---

## 0. How scraper output plugs in

There are four drop-in shapes. Use the first one that fits.

### A. New films and honours for an edition the guide already has (no code change)

Write `data/ext-<scraper>/catalog.json` and add its path to `data/shards.json`. Add a row to `sync.json` with `"id": "ext-<scraper>"`, a `label`, and `updated`/`records` (or a `data/ext-<scraper>/sync.json` stamp `{ "updated": "2026-11-28" }`).

```json
{
  "source": "Festival websites (palmarès pages), checked 2026-11-28",
  "extractor": "external: <scraper name>",
  "festivals": [],
  "films": [
    {
      "id": "ext-cairo-2026-the-film-title",
      "title": "The Film Title",
      "festival": "cairo",
      "year": 2026,
      "format": "Feature",
      "section": "International Competition",
      "country": "Egypt, France",
      "language": "Arabic",
      "credits": [["Director", "Firstname Lastname"]],
      "awards": [["Golden Pyramid", "https://www.ciff.org.eg/...", ""]],
      "sources": ["https://www.ciff.org.eg/..."]
    }
  ],
  "honors": [
    { "festival": "cairo", "year": 2026, "award": ["Faten Hamama Award", "https://www.ciff.org.eg/...", "Person Name"], "role": "Honoree" }
  ]
}
```

Rules the check enforces:
- `id` is unique across every file. Use `ext-<festival>-<year>-<title-slug>`.
- `festival` + `year` must already be an edition (in `catalog.json`, a shard, or `data/announced/announced.json`). If the year is missing, add the edition with shape B first.
- Every URL in `sources` and `awards[][1]` is `https://`.
- `format` is one of `Feature`, `Non-feature`, `Documentary`, `Short film`, `Music video`, `Format unlisted`.
- `credits` are `[role, name]`; `awards` are `[award name, source URL, optional recipient]`. For a person award (Best Director, Best Actress) put the person as the third item.

Not checked, but please do: before writing a film, skip it if the same festival + year already has that title (compare lower-case, accents and punctuation stripped). Otherwise the edition shows it twice.

### B. Dates, edition numbers and juries (no code change)

Add rows to `data/announced/announced.json` under `editions.<festival id>`. Extractors never overwrite this file. A row for a year that already exists only adds fields; a new year adds the edition.

```json
"locarno": [
  { "year": 2026, "number": "79th", "dates": "5–15 August", "source": "https://www.locarnofestival.ch/..." }
],
"redsea": [
  { "year": 2026, "off": "postponed to late 2027", "source": "https://redseafilmfest.com/..." }
]
```

`dates` must parse: `D–D Month` or `D Month–D Month`, with an en dash (`–`), month names in English. Optional `jury: [["Name", "President"], ["Name", ""]]` needs `jurySource`.

### C. A festival the guide does not have yet (no code change)

Put a festival object in the shard's `festivals` list with its films. Use the hand id from `catalog.json` `worldFestivals` where there is one (e.g. `havana`), and add `wikidata`, so the work-in-progress entry is replaced. Do not reuse an id that another file already declares as a festival: ids must be unique.

```json
{
  "id": "havana", "wikidata": "Q1584906", "short": "Havana", "name": "Havana Film Festival (New Latin American Cinema)",
  "region": "Americas", "country": "Cuba", "city": "Havana", "lat": 23.13, "lon": -82.38,
  "description": "Annual festival of Latin American cinema in Havana", "url": "https://habanafilmfestival.com",
  "editions": [{ "year": 2025, "number": "46th", "dates": "4–14 December", "source": "https://habanafilmfestival.com/..." }]
}
```

(Check the QID before using it; this one is an example.)

### D. Extra facts for films the guide already has (needs a small merge first)

Keyed by the existing film `id`, so nothing is duplicated:

```json
{ "source": "...", "films": { "<existing film id>": { "...": "..." } } }
```

The app only merges per-film extras from `data/enrich/films.json` today, and a film's own fields win. Items 6 to 8 below use this shape; when the first such file lands, add a few lines in `app.js` and `check-catalog.mjs` to read it (and have the enrich extractor read item 6's QIDs). Write the file to the schema now; the merge is small.

---

## 1. Results of editions on now or just ended (do first, time-sensitive)

**Why:** these show on the home page "On now" and Calendar. An edition that has ended with no winners looks broken.

| Festival (id) | What is missing | Best source | Shape |
|---|---|---|---|
| Marrakech (`marrakech`) | 2026 awards, announced 28 Nov. The 66 selection films are already in `announced.json`, so add `awards` to those films (same ids, `ann-marrakech-2026-…`) rather than new records | marrakech-festival.com palmarès, then Le360 / Variety | Edit `announced.json` films |
| IFFI Goa (`iffi`) | 2026 line-up and Golden Peacock / ICFT winners (ends 28 Nov). Only the opening film is in | iffigoa.org, pib.gov.in press releases | A |
| Cairo (`cairo`) | 2026, 2025, 2024 competition and winners: 1 film each year now. The "Four Minus Three" 2026 Golden Pyramid row from Wikipedia looks wrong, please check it | ciff.org.eg, Ahram Online | A |
| Black Nights (`poff`) | 2026 and 2025 winners and competition (0 films); 2024 has 2 | poff.ee awards pages | A |
| IDFA (`idfa`) | 2026 edition (Nov 2026) missing entirely; 2025 has 1 film, 2024 has 5 | idfa.nl award winners | B for the edition, then A |
| Tokyo (`tiffjp`) | 2026 edition (Oct–Nov) missing entirely; 2024–25 have no winners | 2026.tiff-jp.net | B, then A |
| Venice (`venice`) | 2026 line-up: only 7 films (2025 has 203) | labiennale.org cinema programme | A |
| Mar del Plata (`mardelplata`) | 2025 and 2024 winners: 1 film each (2026 is done) | mardelplatafilmfest.com, otroscines.com | A |
| Chennai (`ciff-chennai`) | 2026 dates (usually December), not announced on chennaifilmfest.com yet | chennaifilmfest.com, The Hindu | B |
| IFFK, KIFF, Havana (`iffk`, `kiff`, `havana`) | December 2026 line-ups when published; winners on the closing day | iffk.in, kiff.in, habanafilmfestival.com | A (Havana needs C first) |

**Frequency:** daily while a festival is on and for three days after it closes; otherwise weekly.

---

## 2. Missing dates for the Calendar

**Why:** the Calendar and "next up" fall back to "usually in …" when an edition has no `dates`.

- 2026 editions with no dates: `kashish`, `locarno`, `sansebastian`, `hotdocs`, `bfilff`, `miffau`, `ficg`, `venice`, `berlinale`, `tiff`.
- 2027 dates for the festivals that come first next year, as soon as they are announced: `sundance`, `iffr`, `goteborg`, `clermont`, `Q1374050` (Palm Springs), `biffes`, `berlinale`, `fajr`, `sxsw`, `hkiff`, `thessaloniki` (documentary festival in March).
- The 13 hand-listed festivals that are still world-only (`diff`, `jiff`, `oberhausen`, `morelia`, `havana`, `jeonju`, `yidff`, `sgiff`, `kimff`, `dhaka`, `redsea`, `durban`, `iffm`): next edition dates. Five already have 2026 rows.

**Source:** each festival's site (dates are usually in the page title or hero), then the edition's Wikipedia infobox. **Shape:** B. **Frequency:** weekly.

---

## 3. Guide festivals that are empty or thin

**Why:** a festival page with "No films on record yet" is the most visible gap after the home page. Counts are films / films with an award.

| Festival (id) | Now | Pull | Best source |
|---|---|---|---|
| Rajasthan (`rff`) | 0 films, 13 editions (only 11 honourees) | Winners per edition | Festival site / Rajasthan press (Dainik Bhaskar, Rajasthan Patrika). Source is uncertain: confirm one exists before building |
| Clermont-Ferrand (`clermont`) | 0 films, 4 editions | Palmarès per year (Grand Prix national / international / Labo), plus missing editions back to 1979 | clermont-filmfest.org palmarès archive |
| SXSW (`sxsw`) | 0 films in 39 of 40 editions | Film Awards jury and audience winners | sxsw.com film awards pages per year |
| Tribeca (`tribeca`) | 1 film in 25 editions | Founders Award, Best Narrative/Documentary winners | tribecafilm.com festival archive |
| Thessaloniki (`thessaloniki`) | 3 films, 29 empty editions | Golden Alexander and competition | filmfestival.gr archive; Wikipedia "Golden Alexander" |
| Chennai (`ciff-chennai`) | 9 films, editions stop in 2015 | Editions 2016–2025 (B) and Tamil feature competition winners | chennaifilmfest.com, The Hindu |
| Carthage (`Q2545738`) | 11 films, 14 empty editions | Tanit d'Or winners | jcctunisie.org; Wikipedia "Tanit d'Or" |
| FESPACO (`fespaco`) | 147 films, 1 with an award | Étalon de Yennenga and other prizes | fespaco.bf; Wikipedia "Étalon de Yennenga" |
| Fajr (`fajr`) | 71 films, 0 with awards; editions stop in 2023 | Crystal Simorgh winners, 2024–2026 editions | fajrfilmfestival.com; Wikipedia |
| Shanghai (`siff`) | Editions stop in 2018 | 2019–2026 editions and Golden Goblet winners | siff.com |
| Hot Docs (`hotdocs`) | 15 films, 1 per recent year | Award winners per year | hotdocs.ca awards |
| Melbourne (`miffau`), Göteborg (`goteborg`), Warsaw (`Q1578899`) | 0–2 films per recent year | Recent competitions and winners | miff.com.au, goteborgfilmfestival.se, wff.pl |
| Moscow (`Q749235`) | 2026 and 2024 empty | Competition and St. George winners | moscowfilmfestival.ru |
| Seattle (`Q2399132`), Palm Springs 2026 (`Q1374050`), HKIFF (`hkiff`), Busan (`biff`), Toronto (`tiff`) | Line-ups in, winners missing or thin (Busan 2 of 220 in 2026) | Award winners per year | siff.net, psfilmfest.org, hkiff.org.hk, biff.kr, tiff.net |
| Bengaluru Queer (`bqff`) | 83 films, 0 credits | Directors for the 83 titles | Festival programme PDFs |

NYFF and Telluride have no awards because they are non-competitive. Do not chase winners there.

**Shape:** A (B for missing editions). **Frequency:** monthly; these are history and rarely change.

---

## 4. World-only festivals that should become guide festivals

**Why:** 13 hand-listed festivals show on the World list and Map with no films at all: Dharamshala (`diff`), Jaipur (`jiff`), Oberhausen (`oberhausen`), Morelia (`morelia`), Havana (`havana`), Jeonju (`jeonju`), Yamagata (`yidff`), Singapore (`sgiff`), Kathmandu Mountain (`kimff`), Dhaka (`dhaka`), Red Sea (`redsea`), Durban (`durban`), Indian Film Festival of Melbourne (`iffm`).

**Pull:** the festival record, every edition you can find (year, number, dates, source), and at least the main prize winners per edition. Line-ups if the site has them.

**Source:** each festival's archive pages; English Wikipedia list of winners (Havana "Coral award", Morelia "Ojo", Jeonju, Yamagata "Robert and Frances Flaherty Prize").

**Shape:** C (festival plus films in one shard). **Frequency:** monthly.

---

## 5. Indian festival history

**Why:** Indian festivals are the core audience. Today 77 Indian editions have winners on record; many famous ones only cover two or three recent years.

| Festival (id) | Now | Pull |
|---|---|---|
| IFFI (`iffi`) | 2024–2026 only (held since 1952) | Golden Peacock and other winners per edition, editions back to 1952 |
| IFFK (`iffk`) | 2024–2026 only (held since 1996) | Suvarna Chakoram, Rajata Chakoram, FIPRESCI, NETPAC winners per edition |
| KIFF (`kiff`) | 8 films per year, 2012–2025, 3 empty editions | Competition line-ups and winners; dates for 10 editions |
| BIFFes (`biffes`) | Line-ups in, winners missing for 2024 and 2026 and for 7 editions | Winners from biffes.org award pages |
| MAMI (`mami`) | Stops at 2024 | 2025 winners |
| PIFF Pune (`piff`) | Stops at 2022 | 2023–2026 editions and winners; dates for all 17 |
| MIFF Mumbai (`miff`) | 2020–2024 | 2022 and 2026 editions (biennial) and winners |
| IDSFFK (`idsffk`) | 2024 only | 2025 and earlier editions |
| Jagran (`jagran`), GIFF (`giff`), Reel Desires (`ciqff`), All Lights (`aliff`) | 1–3 editions, stale | Recent editions and winners |

**Source:** festival sites, PIB press releases (IFFI), Kerala Chalachitra Academy (IFFK), The Hindu and Indian Express archives. **Shape:** A and B. **Frequency:** monthly; weekly in Nov–Feb festival season.

---

## 6. Films not matched to Wikidata

**Why:** a matched film gets runtime, genres, IMDb link, poster, YouTube trailer, and "Won next" in Award impact. 22,034 of 48,729 films have no Wikidata id. (The often-quoted 9,200 is out of date.)

- By shard: world-editions 11,472, big-five 7,550, rest mostly hand catalogue.
- By festival: Locarno 4,482, Venice 2,912, BIFFes 2,085, Cannes 2,032, Berlinale 1,260, Toronto 1,042, Busan 903, Annecy 627, Rotterdam 529, Sitges 521.

**Pull:** for each unmatched film, its Wikidata QID, with a confidence and the evidence used (title, year, director). Leave a film out rather than guess.

**Source:** Wikidata `wbsearchentities` plus a director check (P57); for films without a Wikidata item, IMDb id (then Wikidata lookup by P345) or TMDB id (P4947).

**Shape:** D at `data/ext-matches/films.json`:

```json
{ "source": "Wikidata search + director check", "films": {
  "wp-q502053-2024-some-film": { "wikidata": "Q123456", "match": "title+year+director", "imdb": "tt1234567" }
} }
```

Only `wikidata` is required (must be `Q` + digits). The enrich extractor then fetches runtime, genres and posters for those ids on its next run. **Frequency:** monthly, after the weekly shards refresh.

---

## 7. Crew beyond directors (Roles tab)

**Why:** Explore > Roles ranks cinematographers, editors, composers, writers and producers, but only 645 films have any non-director credit (almost all from the BIFFes/IFFI/IFFK catalogues), so those lists are near empty.

**Pull:** for award-winning films first (about 7,000), then competition films: Writer, Cinematographer, Editor, Composer, Producer, and up to 5 Actors. Use exactly these role names; the Roles tab groups by them.

**Source:** Wikidata (P58 screenwriter, P344 cinematographer, P1040 editor, P86 composer, P162 producer, P161 cast) for matched films; festival catalogue pages for the rest; TMDB credits as a fallback (facts only, no images).

**Shape:** D at `data/ext-crew/films.json`:

```json
{ "source": "Wikidata P58/P344/P1040/P86/P162/P161", "films": {
  "q135439871-q49024-2025": { "credits": [["Cinematographer", "Name"], ["Editor", "Name"], ["Composer", "Name"]], "sources": ["https://www.wikidata.org/wiki/Q135439871"] }
} }
```

Do not repeat the director; the merge will add these after the film's own credits. **Frequency:** monthly.

---

## 8. Oscar and BAFTA qualifying flags

**Why:** "Which festivals qualify a short for the Oscars or BAFTA" is a common question, and winners of those sections can be marked. Nothing is on record today (oscars.org and bafta.org are blocked from our cloud runs, so this needs your scraper).

**Pull:** per festival and year, the award, category and which prize qualifies.

**Source:** Academy "Short Films Qualifying Festival List" (in the yearly rules on oscars.org), BAFTA short film and short animation qualifying festivals (bafta.org), European Film Awards short film nominee festivals (europeanfilmawards.eu).

**Shape:** D at `data/ext-qualifying/festivals.json`, keyed by guide festival id or world festival QID:

```json
{ "source": "Academy rules 2027, BAFTA 2027 qualifying list", "festivals": {
  "clermont": [
    { "body": "Academy Awards", "category": "Live Action Short", "prize": "Grand Prix (International Competition)", "year": 2027, "source": "https://www.oscars.org/..." },
    { "body": "BAFTA", "category": "British Short Film", "prize": "Any competition selection", "year": 2027, "source": "https://www.bafta.org/..." }
  ]
} }
```

**Frequency:** yearly, when the rules come out (usually spring), plus a monthly check for mid-year changes.

---

## 9. Posters

**Why:** cards look better with art, but only 650 films have artwork and 420 more have a Commons poster.

**Pull:** a poster only where the licence is known and allows reuse (Wikimedia Commons, or press kits that state a licence). TMDB and festival site images are copyrighted, so do not copy them into the repo.

**Source:** Commons search by the film's QID (P3383 first, then Commons categories named after the film); festival press kits with a stated licence.

**Shape:** D at `data/ext-posters/films.json`, with the image saved in `data/ext-posters/posters/`:

```json
{ "films": { "<film id>": { "poster": { "file": "data/ext-posters/posters/<film id>.jpg", "source": "https://commons.wikimedia.org/wiki/File:...", "license": "CC BY-SA 4.0", "licenseUrl": "https://creativecommons.org/licenses/by-sa/4.0/", "credit": "Author, via Wikimedia Commons" } } } }
```

Use a 330 px wide thumbnail (upload.wikimedia.org only serves standard widths). **Frequency:** monthly. Lowest priority because licensed posters are rare.

---

## Ranking at a glance

1. Results of editions on now or just ended (Marrakech, IFFI, Cairo, Black Nights, IDFA, Tokyo, Venice 2026)
2. Missing 2026 and 2027 dates (Calendar)
3. Empty and thin guide festivals (Rajasthan, Clermont-Ferrand, SXSW, Tribeca, Thessaloniki, Chennai, Carthage, FESPACO, Fajr, Shanghai …)
4. 13 world-only festivals into the guide
5. Indian festival history (IFFI and IFFK back catalogues first)
6. Wikidata matches for 22,034 films
7. Crew beyond directors
8. Oscar and BAFTA qualifying flags
9. Posters

Items 1 to 5 drop in with no code change. Items 6 to 9 need a small merge added when their first file lands.
