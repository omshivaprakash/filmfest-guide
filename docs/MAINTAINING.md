# Maintaining

How to refresh data, run an extractor by hand, add a festival and publish. Read [How it works](HOW-IT-WORKS.md) first.

## Before and after every change

```
node --check app.js && node check-catalog.mjs
python3 -m http.server 8000      # then open http://localhost:8000
```

`check-catalog.mjs` prints the totals (films, festivals, world festivals) and stops with an error if anything is broken. GitHub runs the same check on every push and pull request (`.github/workflows/check.yml`).

Publishing is merging to `main`: GitHub Pages serves the repository root. Bump `VERSION` in `sw.js` when `index.html`, `style.css`, `app.js` or `geo.js` change, so installed copies refresh.

---

## Extractors

An **extractor** reads one source (a festival's site or catalogue, Wikidata, the Internet Archive) and writes one **shard** of data. Keeping one source per extractor and one shard per source means extractors can run on their own schedules without touching each other's files.

```
tools/extractors/<name>/
    extract.py        # reads the source, writes data/<name>/
    README.md         # what it reads, how often the source changes, known gaps
data/<name>/          # the shard: JSON with the field names in the Data dictionary
.github/workflows/<name>.yml   # runs the extractor on a schedule
```

Rules for an extractor:

- Write only inside `data/<name>/`. Never edit another shard.
- Use the field names in the [Data dictionary](DATA-DICTIONARY.md), and keep a source URL with every record.
- Be polite to the source: identify the client in the `User-Agent`, pause between requests, and cache downloads so a rerun does not fetch everything again.
- Be safe to run twice: the same input gives the same output, so a scheduled run that finds nothing new commits nothing.

### Run an extractor by hand

```
python3 tools/extractors/<name>/extract.py
node check-catalog.mjs
git diff --stat data/<name>/
```

Read the extractor's own README for any arguments (for example a cache folder) and the Python packages it needs.

### Scheduled refreshes

Every extractor's workflow is a short caller of the shared [`.github/workflows/extract.yml`](../.github/workflows/extract.yml):

```yaml
name: <name>
on:
  schedule: [{ cron: '17 3 * * 1' }]   # UTC; spread start minutes
  workflow_dispatch:
permissions: { contents: write }
jobs:
  sync:
    uses: ./.github/workflows/extract.yml
    with: { name: <name>, packages: 'pymupdf lxml', args: '' }
```

The shared workflow:

1. runs `tools/extractors/<name>/extract.py` with `args`, after installing `packages`;
2. stops quietly if nothing in `data/<name>/` changed;
3. otherwise stamps `data/<name>/sync.json` with the time and record count (`tools/mark-synced.py`), runs `node --check app.js && node check-catalog.mjs`, and commits and pushes as omshivaprakash, so the site updates itself.

Runs share one concurrency group, so two extractors never push at the same time. If a run fails, nothing is committed and the site keeps the last good data; the workflow's log in the Actions tab says which source failed. Any workflow can also be started by hand from **Actions → the workflow → Run workflow**.

**Data freshness.** The root `sync.json` lists every source with its `label` and `schedule`, and the home page's Data freshness panel reads it. A scheduled extractor adds a row `{ "id": "<name>", "label": "…", "schedule": "weekly" }` and leaves out `updated`, which comes from `data/<name>/sync.json`. Hand-run importers (the festival catalogues) carry `updated` and `records` in the root file; update them when you rerun one.

| Extractor | Source | Workflow | Schedule (UTC) |
|---|---|---|---|
| world-festivals | Wikidata, English Wikipedia, Wikimedia Commons | world-festivals.yml | Mondays 03:17 |
| youtube-links | Wikidata (P1651) | youtube-links.yml | Wednesdays 04:23 |

Pick a schedule that matches how often the source changes: daily during a festival's programme announcements, weekly for Wikidata, monthly for archives that rarely change. Spread start times so runs do not all start at once.

---

## The original importers

These read one source each and write straight into `catalog.json`. They run by hand. (The world list and YouTube links are now scheduled extractors; their commands are kept here for running by hand.)

### World festivals from Wikidata

```
python3 tools/extractors/world-festivals/extract.py [cache-dir]         # fetch then build, as the weekly workflow does
python3 tools/extractors/world-festivals/extract.py fetch <cache-dir>   # query Wikidata, Wikipedia and Commons (slow, polite)
python3 tools/extractors/world-festivals/extract.py build <cache-dir>   # write data/world-festivals/ (list, descriptions, logos)
python3 tools/extractors/world-festivals/extract.py kinds <cache-dir>   # refresh the classes used for festival types
```

Festivals are Wikidata items that are an instance of "film festival" (Q220505) or a common subclass, excluding single editions. The app loads the list after the first screen and merges in the hand-checked `worldFestivals` from `catalog.json`, which add the usual month. Each logo keeps its own licence and credit.

### YouTube links

```
python3 tools/extractors/youtube-links/extract.py [cache-dir]
```

Matches catalogue films to Wikidata films with a YouTube video ID (P1651) by title, year within two and director (or country when there is no director), and writes `data/youtube-links/youtube.json`; the app adds `youtube` and `wikidata` to each matched film when it loads.

### Bengaluru catalogues

Official catalogue URLs for the 17 editions are in `tools/biffes-sources.json`, keyed by edition number. Convert downloaded catalogues to `1.txt` through `17.txt` with `pdftotext -layout`. The optional `4-ocr.txt` is the searchable text from Internet Archive item `unset0000unse_n1n9`, and `9-ocr.txt` is layout text from the searchable PDF on item `biffes.9th-biffes-catalogue-2017`. Then:

```
python3 tools/import-biffes.py <text-directory> catalog.json
```

The importer adds printed page references for index-only entries and PDF page links for matching film pages. Scanned and irregular layouts can leave gaps.

### Bengaluru: Servants of Knowledge archive

Save the 2022 and 2023 screening schedule PDFs as `schedule2022.pdf` and `schedule2023.pdf`, and the retrospective awards PDF as `awards2020.txt` (via `pdftotext -layout`). After the catalogue import, run:

```
python3 tools/import-sok-biffes.py <source-directory> catalog.json
```

Needs PyMuPDF. Entries point to individual scan pages. The image-only 2014 and 2020 schedules are available through the document links.

### Goa and Kerala

With PyMuPDF and lxml installed, put in one folder the PIB Indian Panorama pages as `iffi24.html` and `iffi25.html`, the 30th IFFK screening schedule as `iffk25.pdf`, and OCR of the 16th IDSFFK official selection as `ocr/page-01.txt` to `ocr/page-16.txt`. Then:

```
python3 tools/import-goa-kerala.py <source-directory> catalog.json
```

It reads the 29th IFFK section selections from `tools/iffk-2024-selections.tsv`.

---

## Adding a festival

1. Add it to `festivals` in `catalog.json` with `id`, `name`, `short`, `region`, `country`, `lat`, `lon`, `url`, `description` and its `editions`.
2. If it was in `worldFestivals`, remove it from there (ids must be unique).
3. Write an extractor for its catalogue in `tools/extractors/<id>/`, with a shard in `data/<id>/` and a scheduled workflow.
4. Add its logo to `assets/` or `images/`, with the source.
5. Add any new country's position to `POS` in `geo.js`, so the map can place it.
6. Run the checks, look at it in the browser, and add a section to [Data notes](DATA-NOTES.md).

## Hand edits

You can fix a title, credit or award directly in `catalog.json`. Keep the source URL with the claim it supports, and note the fix in the commit message. If the record came from an extractor, fix the extractor too, or the next scheduled run will undo the edit.
