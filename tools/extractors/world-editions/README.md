# World festivals extractor

Writes `data/world-editions/catalog.json`: editions, line-ups, award winners and nominated films for about 40 major festivals outside the Big Five (Cannes, Venice, Berlin, Toronto and Sundance have their own extractor).

```
python3 tools/extractors/world-editions/extract.py           # query Wikidata and write the shard (about 2 minutes)
python3 tools/extractors/world-editions/extract.py --check   # self-test only, no network
```

Standard library only. The Wikipedia step is in `wikipedia.py`. Runs weekly from `.github/workflows/world-editions.yml` (Mondays 04:17 UTC).

## What it reads

All from the Wikidata Query Service (CC0), about a dozen queries with a pause between each:

- **Editions**: items that are part of the festival series (P179 or P361) with an edition number (P393) or typed as a film festival edition. Year from the start date (P580) or point in time (P585); dates when the start and end are known to the day.
- **Awards**: items linked to the festival by conferred by (P1027) or part of (P361), followed through award groups. `EXTRA_AWARDS` adds prizes whose items are not linked back (Golden George, Moscow).
- **Winners** (P166) and **nominees** (P1411) of those awards, dated by the statement's point in time (P585) or its edition (P805). Films become `films`; people become `honors`.

Then, from **English Wikipedia** edition articles (the ones Wikidata links, about 270), `wikipedia.py` reads:

- **Line-ups**: every wikitable under a programme section that has a title and a director column (jury, industry and academy sections are skipped). Each row becomes a film with its `section`, director and country.
- **Awards**: bulleted `Award: ''Film'' by Director` lines under award sections. Films are matched to the Wikidata records by title within the edition.

And from each festival's **main English Wikipedia article** and the articles of its **awards** (those with an English sitelink), year-by-year winner tables with a year, a title and a director column. In a main article only award sections count, and the award is the section heading. A table where a year repeats lists nominees or ties, so it is skipped; only italicised titles count, so "not held" rows are dropped. A winner with no edition on record adds that edition, sourced to the list.

Each festival keeps its Wikidata QID in `wikidata`; festivals hand-listed in catalog.json keep that id, so the imported festival replaces its entry from `world-festivals.json`. Name, place, logo and description come from `data/world-festivals/world-festivals.json`.

## Licence

Wikidata is CC0. From Wikipedia (CC BY-SA 4.0) only facts are taken: titles, directors, countries, sections and awards, never prose. Every film links to its Wikidata item or its Wikipedia article, and every edition links the article it came from.

## Known gaps

Coverage is only as good as Wikidata. Busan, Shanghai, Mar del Plata, Clermont-Ferrand, London and New York have editions but few or no dated winners there. Wikipedia line-ups exist for about 270 editions, mostly recent ones; Busan, NYFF, Seattle, Hong Kong, FESPACO and Fajr pages have line-ups but awards in prose or tables the parser does not read yet. Tables with merged (rowspan) cells lose those rows. Most Wikipedia-only films have no format. To add a festival, put its QID and short name in `FESTIVALS`.
