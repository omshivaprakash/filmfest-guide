# FilmFest Guide

[Open FilmFest Guide](https://omshivaprakash.github.io/filmfest-guide/)

A dependency-free festival archive, inspired by the [LitFest Speaker Guide](https://github.com/omshivaprakash/litfest-speaker-guide).

Run `python3 -m http.server 8000 --directory dist` from this folder and open http://localhost:8000.

Edit `dist/catalog.json` to extend the starter archive. Editions belong to festival IDs. Films link to an edition by festival ID and year. Each credit pairs a role with a name. Film awards can include a named recipient, and standalone awards can list a person without a film. Add source URLs alongside the claims they support. The archive displays selected records and derives the people directory from the credited names.

Run `node --check dist/app.js` and `node check-catalog.mjs` after editing.

## Bengaluru archive import

Official catalogue URLs for the 17 editions are in `tools/biffes-sources.json`, keyed by edition number. Convert downloaded catalogues to `1.txt` through `17.txt` with `pdftotext -layout`. The optional `4-ocr.txt` is the searchable text from Internet Archive item `unset0000unse_n1n9`. The optional `9-ocr.txt` is layout text from the searchable PDF linked on Internet Archive item `biffes.9th-biffes-catalogue-2017`. Run `python3 tools/import-biffes.py <text-directory> dist/catalog.json` to rebuild the extracted entries.

The importer adds printed page references for index-only entries and PDF page links for matching film pages. Scanned and irregular layouts can leave gaps. A PDF link in the edition selector indicates a source is available, even when no titles could be extracted from it. Portraits have source and license credits in their profile. Profiles without a sourced portrait use initials.

## Goa and Kerala programme import

Run `python3 tools/import-goa-kerala.py <source-directory> dist/catalog.json` with PyMuPDF and lxml installed. The source directory contains the PIB Indian Panorama pages as `iffi24.html` and `iffi25.html`, the 30th IFFK screening schedule as `iffk25.pdf`, and OCR from the 16th IDSFFK official selection as `ocr/page-01.txt` through `ocr/page-16.txt`. The importer includes source URLs and reads the 29th IFFK section selections from `tools/iffk-2024-selections.tsv`.

Goa coverage includes Indian Panorama and selected award winners. Kerala coverage includes three sections of the 29th IFFK, the extracted 30th IFFK schedule, and the extracted 16th IDSFFK official selection. Scanned or irregular source layouts can leave gaps.

## Servants of Knowledge archive

The Bengaluru festival selector includes an **Archive documents** menu for the Internet Archive catalogues, schedules and awards. The data import reads the 2022 and 2023 screening schedule PDFs and the retrospective awards PDF using `tools/import-sok-biffes.py` and PyMuPDF. Save the two PDFs as `schedule2022.pdf` and `schedule2023.pdf` alongside `awards2020.txt`, produced with `pdftotext -layout` from the awards PDF. Run `python3 tools/import-sok-biffes.py <source-directory> dist/catalog.json` after the Bengaluru catalogue import. Entries point to individual scan pages. The image-only 2014 and 2020 schedules are available through the document links.
