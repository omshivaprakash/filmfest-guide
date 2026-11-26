# World festivals extractor

Writes `data/world-editions/catalog.json`: editions, award winners and nominated films for about 40 major festivals outside the Big Five (Cannes, Venice, Berlin, Toronto and Sundance have their own extractor).

```
python3 tools/extractors/world-editions/extract.py           # query Wikidata and write the shard (about 2 minutes)
python3 tools/extractors/world-editions/extract.py --check   # self-test only, no network
```

Standard library only. Runs weekly from `.github/workflows/world-editions.yml` (Mondays 04:17 UTC).

## What it reads

All from the Wikidata Query Service (CC0), about a dozen queries with a pause between each:

- **Editions**: items that are part of the festival series (P179 or P361) with an edition number (P393) or typed as a film festival edition. Year from the start date (P580) or point in time (P585); dates when the start and end are known to the day.
- **Awards**: items linked to the festival by conferred by (P1027) or part of (P361), followed through award groups. `EXTRA_AWARDS` adds prizes whose items are not linked back (Golden George, Moscow).
- **Winners** (P166) and **nominees** (P1411) of those awards, dated by the statement's point in time (P585) or its edition (P805). Films become `films`; people become `honors`.

Festival ids are Wikidata QIDs, so an imported festival replaces its entry from `world-festivals.json`. Name, place, logo and description come from `data/world-festivals/world-festivals.json`.

## Licence

Wikidata is CC0. Every record links to its Wikidata item and, where one exists, its English Wikipedia article; no Wikipedia text is copied.

## Known gaps

Coverage is only as good as Wikidata. Busan, Shanghai, Mar del Plata, Clermont-Ferrand, London and New York have editions but few or no dated winners there. Full selections (every film shown) are not in Wikidata for most festivals; the next step is reading the edition articles on Wikipedia. To add a festival, put its QID and short name in `FESTIVALS`.
