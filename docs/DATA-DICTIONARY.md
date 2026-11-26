# Data dictionary

What every field in the data files means. Useful if you want to reuse the data, fix an entry by hand, or add a festival.

All data files are plain **JSON** (text files that any program can read). The facts are CC BY 4.0; see [LICENSE-DATA.md](../LICENSE-DATA.md).

---

## 1. `catalog.json`

```json
{ "festivals": [...], "films": [...], "honors": [...], "portraits": {...}, "worldFestivals": [...] }
```

### `festivals[]`: festivals in the guide

| Field | Meaning |
|---|---|
| `id` | Short code used in web addresses, e.g. `biffes` → `?f=biffes` |
| `name`, `short` | Full name, and the short name for chips and buttons |
| `region`, `country` | Where it is held (city or state, and country) |
| `lat`, `lon` | Map position |
| `description` | One line on what it screens |
| `url` | Official website |
| `logo` | Logo path |
| `editions[]` | One entry per edition (below) |

### `festivals[].editions[]`

| Field | Meaning |
|---|---|
| `year`, `number` | Edition year, and its ordinal as the festival counts it (`17th`) |
| `dates` | Human-readable dates |
| `catalogue`, `catalogueLabel` | Link to the edition's catalogue or programme, and an optional label for it |
| `source` | Main source page for the edition |
| `importedTitles` | How many titles the importer read from the source |
| `archiveDocuments[]` | Extra scans, as `{ "name", "url" }` (Internet Archive) |

### `films[]`

| Field | Meaning |
|---|---|
| `id` | Stable id, `<festival>-<year>-<n>` |
| `title` | Title as printed in the source |
| `festival`, `year` | The edition it screened at (must exist in `festivals`) |
| `format` | `Feature`, `Non-feature`, `Documentary`, `Short film`, `Music video`, or `Format unlisted` |
| `section` | Festival section, e.g. `International Competition` |
| `language`, `country` | As printed, comma-separated; countries are tidied to one spelling |
| `summary` | Short synopsis, where the source has one (owned by the festival or filmmaker) |
| `credits` | List of `[role, name]` pairs, e.g. `["Director", "Payal Kapadia"]` |
| `awards` | List of `[award name, source URL, optional recipient]` |
| `sources` | Source URLs, often with `#page=` into the catalogue PDF |
| `cataloguePage` | Printed page number for index-only entries |
| `artwork` | `{ file, source, ... }` still or poster, with its source |
| `wikidata` | Wikidata id (`Q…`) where the film was matched |
| `youtube` | List of `[video id, "trailer" or "video"]` from Wikidata; added on load from `data/youtube-links/youtube.json` |
| `fromCatalogue`, `fromGoaKeralaImport` | Marks which importer wrote the record |

### `honors[]`: awards to a person, not a film

`{ "festival", "year", "award": [name, source URL, recipient], "role" }`

### `portraits`

Keyed by person name: `{ file, source, credit, license, licenseName }`. Only photos with a known source and licence are used; everyone else gets initials.

### `worldFestivals[]`: hand-checked festivals still to add

`id`, `name`, `short`, `city`, `country`, `region`, `lat`, `lon`, `month` (usual month), `url`, and `status: "wip"`.

---

## 2. `data/world-festivals/world-festivals.json`

```json
{ "source": "...", "retrieved": "2026-11-26", "festivals": [...] }
```

| Field | Meaning |
|---|---|
| `id` | Wikidata id (`Q…`), so every row can be traced and fixed at the source |
| `name`, `desc` | Label and short Wikidata description |
| `country`, `city`, `region` | Where it is held; region is worked out from the country |
| `ll` | `[longitude, latitude]` |
| `since` | Year founded, where known |
| `url` | Official website |
| `types` | Festival types (see [Data notes](DATA-NOTES.md#world-festivals-work-in-progress)) |
| `links` | Number of Wikipedia and sister-project articles about it (Wikidata sitelinks), used to sort by prominence |
| `wiki` | English Wikipedia article |
| `logo` | `{ file, source, credit, license, licenseUrl }` from Wikimedia Commons |

## 3. `data/world-festivals/world-about.json`

`{ "<Wikidata id>": "Opening paragraph of the English Wikipedia article" }`. CC BY-SA 4.0, loaded only when a festival is opened.

## 4. Extractor shards: `data/<name>/`

Each extractor in `tools/extractors/<name>/` writes only to its own folder in `data/<name>/`. A shard uses the same field names as the matching list above (films, editions or festivals), so the app and `check-catalog.mjs` read it the same way. A shard of festivals, films and honours is `data/<name>/catalog.json` in the shape of `catalog.json`; list its path in `data/shards.json` and the app merges it in. A shard festival with `wikidata` (or an `id` matching a hand-listed entry) comes off the work in progress list. An extractor's own README describes anything extra it writes.
