# youtube-links

YouTube videos for catalogue films, as recorded on Wikidata.

- **Source:** Wikidata (CC0), "YouTube video ID" (P1651) on films, with the "trailer" role qualifier when present.
- **Output:** `data/youtube-links/youtube.json`: catalogue film id → `{wikidata, youtube: [[video id, "trailer" | "video"]]}`. The app merges it into `catalog.json` films on load.
- **Run:** `python3 tools/extractors/youtube-links/extract.py [cache-dir]`.
- **Matching:** title, year within two, and director (or country when the catalogue has no director credit).
- **Known gaps:** only what Wikidata records; most links are trailers, and full films are rare.
