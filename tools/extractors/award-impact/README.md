# award-impact

What festival award winners in the guide went on to win, as recorded on Wikidata. Feeds Explore › Award impact.

- **Source:** Wikidata (CC0): "award received" (P166) and "nominated for" (P1411), with "point in time" (P585).
- **Input:** films in `catalog.json` and the shards in `data/shards.json` that won a festival award and have a Wikidata id (their own, or one matched by youtube-links).
- **Output:** `data/award-impact/impact.json`: `{count, films: {QID: {won: [[award, award QID, year | null]], nominated: [...]}}}`.
- **Run:** `python3 tools/extractors/award-impact/extract.py [cache-dir]`. Weekly, Wednesdays 05:41 UTC.
- **In the app:** awards dated the festival year or later, other than the film's own festival awards, count as "won next". Undated awards and films without a Wikidata id are shown as not checked; nothing is inferred.
- **Known gaps:** catalogue films from BIFFes, IFFI and IFFK rarely have Wikidata ids, so Indian winners are mostly unchecked.
