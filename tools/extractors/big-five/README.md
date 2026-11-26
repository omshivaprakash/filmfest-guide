# Big Five extractor

Writes `data/big-five/catalog.json`: editions, line-ups, award winners and nominated films for Cannes, Venice, Berlin, Toronto and Sundance.

```
python3 tools/extractors/big-five/extract.py           # query Wikidata and Wikipedia and write the shard (about 6 minutes)
python3 tools/extractors/big-five/extract.py --check   # self-test only, no network
```

It reuses `tools/extractors/world-editions/extract.py` with its own festival list, so the sources, rules, licence and known gaps are the ones in that extractor's README. Runs weekly from `.github/workflows/big-five.yml` (Mondays 04:47 UTC).

Festivals keep their catalog.json ids (`cannes`, `venice`, `berlinale`, `tiff`, `sundance`), so each replaces its work-in-progress entry.

## Known gaps

Wikidata dates only some winners: about 33 Palme d'Or winners and 10 Toronto People's Choice awards are dated there. Toronto awards no juried competition prizes, so it shows few winners. Line-ups come from English Wikipedia edition articles, mostly from the 2000s on.
