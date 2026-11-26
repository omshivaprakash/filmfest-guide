# Indian festivals extractor

Writes `data/india/catalog.json`, a shard in the same shape as `catalog.json` (`festivals`, `films`, `honors`), for Indian festivals that are not in the hand-built catalogue: Kolkata (KIFF), MAMI Mumbai, Chennai (CIFF), Pune (PIFF), MIFF Mumbai (documentary, short and animation), KASHISH, Dharamshala, Jaipur, Jagran, Guwahati, the International Children's Film Festival and Osian's Cinefan. The list is `FESTIVALS` at the top of `extract.py`.

```
pip install lxml
python3 tools/extractors/india/extract.py          # fetch into .cache/india, then build the shard
python3 tools/extractors/india/extract.py test     # parser self-check
node check-catalog.mjs
```

`fetch <cache>` and `build <cache>` run the two halves separately. Downloads already in the cache are not fetched again, so delete the cache to pick up new edits.

## What it reads

- **English Wikipedia**, one article per festival through the REST page HTML endpoint (about 12 requests, 5 seconds apart; `action=parse` is refused to cloud runners): award tables with one row per edition and one column per award (Kolkata), Category and Winner tables under an edition heading (Chennai), `YEAR: Title - Director | Country` lists under an award heading (KASHISH), and jury tables (KASHISH). Film titles are the italic text in a cell; "Person for *Film*" gives a recipient, "*Film* by Person" a director.
- **Wikidata** (two or three SPARQL queries): edition items of each festival, and for each film the article links, its language, country, director, format and a one-line description.

- **`checked.json`**, hand-checked winners for festivals whose Wikipedia article has no award table (MAMI 2023 and 2024, MIFF 2024, Jagran 2025, Guwahati 2017). Each record keeps the page it was read from, which may be a press report rather than official results, and a `checked` date. These carry through to the shard as `checked: "checked online <date>"`. Add a record there when you confirm a result. Leave out fees and deadlines.

Every film, honour and edition links the Wikipedia revision it came from. Only facts are kept (titles, names, years, award names). Wikidata is CC0; Wikipedia is CC BY-SA 4.0. Logos are reused from `world-festivals.json` with their Commons licence.

Festival ids match the hand-listed `worldFestivals` ids, and `wikidata` matches the `data/world-festivals/world-festivals.json` row, so the app takes an imported festival off the work in progress list.

## Schedule

`.github/workflows/india.yml` calls the shared `extract.yml` every Tuesday at 04:23 UTC (and on demand from the Actions tab). It commits `data/india/` only when it changed. Wikipedia articles for these festivals change a few times a month at most.

## Known gaps

- Official festival sites and PIB are not reachable from the cloud session used to build this, so their results are added by hand in `checked.json` from press reports for now. Dharamshala is non-competitive, and Jaipur has no results source yet.
- A film linked through a Wikipedia redirect gets no Wikidata details (language, country, summary).
- Juries are stored on each edition (`jury`) but the app does not show them yet.
