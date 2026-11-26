# world-editions

Editions, award winners, nominees and selected films of the 40 best-known world festivals (by Wikipedia language editions in `data/world-festivals/world-festivals.json`).

- **Source:** Wikidata (CC0). Editions are items that are a "film festival edition" (Q27787439) in the festival's series. Winners and nominees come from "award received" (P166) and "nominated for" (P1411) on films, for awards conferred by or part of the festival. Selected films come from "presented works" (P13360) on an edition, or "participant in" (P1344) on a film.
- **Output:** `data/world-editions/world-films.json`: `festivals` maps a festival's Wikidata id to `editions` (`[year, edition number, start, end]`) and `films` (`[film id, year, "won" | "nominated" | "selected", [award names]]`); `films` maps a film's Wikidata id to `[title, year, directors, countries, youtube ids?]`.
- **Run:** `python3 tools/extractors/world-editions/extract.py [cache-dir] [count]`. Responses are cached in the cache folder (default `.cache/world-editions`); delete it to fetch fresh data.
- **How often the source changes:** winners are added within days of each festival; weekly is enough.
- **Known gaps:** coverage follows Wikidata. Cannes, Berlin, Venice, Annecy, Rotterdam and Sitges are well covered; many festivals record editions but few films, and juries are rarely recorded, so they are not imported yet.
