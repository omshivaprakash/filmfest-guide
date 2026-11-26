# FilmFest Guide

[Open FilmFest Guide](https://omshivaprakash.github.io/filmfest-guide/)

**Films, the people who made them, awards and past editions from film festivals, starting with India.** A companion to the [LitFest Guide](https://github.com/omshivaprakash/litfest-speaker-guide), built the same way: one static page, no build step, no account, works offline after the first visit.

## Layout

Same structure as LitFest Guide:

| You want to… | Where to go |
|---|---|
| See every festival at a glance | **Home** (the **All** chip) |
| Open a festival: latest edition, films per year, where to start | Festival chip, **Discover** tab |
| Browse films, people or awards for that festival | **Films**, **People**, **Awards** tabs |
| See every edition with its catalogue and archive documents | **Past years** tab |
| Look up a film or person across every festival | **Search** (top bar) |
| See where the films and their makers come from, on a world map | **Explore → Map** (Films, People, Festivals), or a festival's **Map** tab |
| See which languages the films are in | **Explore → Languages** |
| Find filmmakers who return across festivals and editions | **Explore → Across festivals** |
| See the festivals worldwide that are listed and still to be added | **Explore → World festivals**, or the work in progress card on Home |

Every view fits one screen and pages instead of scrolling. Links are shareable: `?f=biffes` opens a festival and `#films`, `#people`, `#awards` or `#years` opens a tab.

## Files

`index.html`, `style.css` and `app.js` are the whole app, with map outlines and country positions in `geo.js`. `catalog.json` holds the data and `images/` the artwork and portraits. `fonts/`, `assets/`, `manifest.webmanifest` and `sw.js` match LitFest Guide (Fraunces and Inter, installable, offline). GitHub Pages serves the repository root from `main`.

Run `python3 -m http.server 8000` from this folder and open http://localhost:8000.

Edit `catalog.json` to extend the starter archive. Editions belong to festival IDs. Films link to an edition by festival ID and year. Each credit pairs a role with a name. Film awards can include a named recipient, and standalone awards can list a person without a film. Add source URLs alongside the claims they support. The archive displays selected records and derives the people directory from the credited names.

Run `node --check app.js` and `node check-catalog.mjs` after editing.

## World festivals (work in progress)

`worldFestivals` in `catalog.json` lists major film festivals that are not imported yet, each with city, country, region, coordinates, usual month and official site. They appear on the Explore map and the World festivals list. To import one, add it to `festivals` with its editions and films, and remove it from `worldFestivals`. `check-catalog.mjs` checks ids are unique and every festival has coordinates.

The wider list, `world-festivals.json`, holds about 8,000 film festivals from Wikidata, with descriptions from English Wikipedia (in `world-about.json`, loaded only when a festival is opened) and logos from Wikimedia Commons in `images/world/` (each logo keeps its own licence and credit). The app loads it after the first screen and merges in the hand-checked `worldFestivals`, which add the usual month. Each festival gets `types` (documentary, short, animation, LGBTQ+, genre and so on) from its Wikidata classes and genres plus words in its name and description; `python3 tools/import-world-festivals.py kinds <cache>` refreshes the classes. Rebuild it with `python3 tools/import-world-festivals.py fetch <cache>` then `build <cache>`.

The `youtube` field on a film lists YouTube videos (trailers or full films) that Wikidata records for it, matched by title, year and director with `python3 tools/link-youtube.py <cache>`. Films → On YouTube lists them.

## Licence

Code is MIT ([LICENSE](LICENSE)). Data is CC BY 4.0 with the exceptions in [LICENSE-DATA.md](LICENSE-DATA.md). Cite it with [CITATION.cff](CITATION.cff).

Film countries in `catalog.json` are normalised to one spelling per country (for example `USA`, `Usa` and `United States` all become `United States`) so the map can count them. Add any new country's position to `POS` in `geo.js`.

## Bengaluru archive import

Official catalogue URLs for the 17 editions are in `tools/biffes-sources.json`, keyed by edition number. Convert downloaded catalogues to `1.txt` through `17.txt` with `pdftotext -layout`. The optional `4-ocr.txt` is the searchable text from Internet Archive item `unset0000unse_n1n9`. The optional `9-ocr.txt` is layout text from the searchable PDF linked on Internet Archive item `biffes.9th-biffes-catalogue-2017`. Run `python3 tools/import-biffes.py <text-directory> catalog.json` to rebuild the extracted entries.

The importer adds printed page references for index-only entries and PDF page links for matching film pages. Scanned and irregular layouts can leave gaps. A PDF link in the edition selector indicates a source is available, even when no titles could be extracted from it. Portraits have source and license credits in their profile. Profiles without a sourced portrait use initials.

## Goa and Kerala programme import

Run `python3 tools/import-goa-kerala.py <source-directory> catalog.json` with PyMuPDF and lxml installed. The source directory contains the PIB Indian Panorama pages as `iffi24.html` and `iffi25.html`, the 30th IFFK screening schedule as `iffk25.pdf`, and OCR from the 16th IDSFFK official selection as `ocr/page-01.txt` through `ocr/page-16.txt`. The importer includes source URLs and reads the 29th IFFK section selections from `tools/iffk-2024-selections.tsv`.

Goa coverage includes Indian Panorama and selected award winners. Kerala coverage includes three sections of the 29th IFFK, the extracted 30th IFFK schedule, and the extracted 16th IDSFFK official selection. Scanned or irregular source layouts can leave gaps.

## Servants of Knowledge archive

The Bengaluru festival selector includes an **Archive documents** menu for the Internet Archive catalogues, schedules and awards. The data import reads the 2022 and 2023 screening schedule PDFs and the retrospective awards PDF using `tools/import-sok-biffes.py` and PyMuPDF. Save the two PDFs as `schedule2022.pdf` and `schedule2023.pdf` alongside `awards2020.txt`, produced with `pdftotext -layout` from the awards PDF. Run `python3 tools/import-sok-biffes.py <source-directory> catalog.json` after the Bengaluru catalogue import. Entries point to individual scan pages. The image-only 2014 and 2020 schedules are available through the document links.
