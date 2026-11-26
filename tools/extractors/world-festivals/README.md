# world-festivals

Every film festival on Wikidata, with types, descriptions and logos.

- **Sources:** Wikidata (CC0): items that are a "film festival" (Q220505) or a common subclass, excluding single editions; English Wikipedia (CC BY-SA 4.0) for the two-sentence descriptions; Wikimedia Commons for logos, each with its own licence and credit.
- **Output:** `data/world-festivals/world-festivals.json` (the list), `world-about.json` (descriptions by Wikidata id) and `logos/<id>.webp`.
- **Run:** `python3 tools/extractors/world-festivals/extract.py [cache-dir]` fetches and builds. `fetch`, `build` and `kinds` run one step: `extract.py build <cache-dir>`. Needs Pillow for new logos (at most 60 new logos a run, so Commons is not hammered).
- **Politeness:** batched SPARQL queries, 20 Wikipedia titles and 40 Commons files per request, a pause between requests, and logos are only downloaded once.
- **Safety:** the build refuses to write if it finds over 5% fewer festivals than the published list, and keeps last week's description wherever Wikipedia rate-limited this run.
- **Known gaps:** about half the festivals have no coordinates on Wikidata and are placed at their country's centre (`approx`). Types come partly from name keywords, so some are missed or wrong.
