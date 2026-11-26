# enrich

Adds detail to festivals and films already in the guide. Writes only `data/enrich/`.

| Output | Per | Fields | Source |
|---|---|---|---|
| `festivals.json` | world festival (Wikidata id) | `fiapf` (`A-list` or `Accredited`), `month`, `every`, `langs`, `editions`, `desc`, `wiki` (non-English) | Wikidata (CC0), English Wikipedia FIAPF article |
| `about.json` | world festival with no English article | `{lang, text}` opening sentences | that Wikipedia (CC BY-SA 4.0, linked by `wiki`) |
| `films.json` | film id | `wikidata`, `minutes`, `genres`, `imdb`, `poster` (Commons image copied to `posters/`, with licence and credit, only for films without artwork) | Wikidata, Wikimedia Commons |

```
python3 tools/extractors/enrich/extract.py test
python3 tools/extractors/enrich/extract.py fetch <cache>
python3 tools/extractors/enrich/extract.py build <cache>
```

Films from `catalog.json` and the India shard are matched on title, a year within two and the same director (or the same country and a year within one when either side has no director); two equal matches leave the film unlinked. Films that already carry a Wikidata id (world-editions) are used as they are; the other world-editions films are not title-matched yet. YouTube links stay with the youtube-links extractor. Requests are spaced (`ENRICH_GAP`, `ENRICH_WDQS_GAP` seconds) and back off on 429; replies are cached, so a rerun resumes. `run` does fetch and build with a fresh temporary cache; `.github/workflows/enrich.yml` calls it monthly (2nd, 04:41 UTC) through the shared `extract.yml`.
