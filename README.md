# FilmFest Guide

A dependency-free festival archive, inspired by the [LitFest Speaker Guide](https://github.com/omshivaprakash/litfest-speaker-guide).

Run `python3 -m http.server 8000 --directory dist` from this folder and open http://localhost:8000.

Edit `dist/catalog.json` to extend the starter archive. Editions belong to festival IDs. Films link to an edition by festival ID and year. Each credit pairs a role with a name. Film awards can include a named recipient, and standalone awards can list a person without a film. Add source URLs alongside the claims they support. The archive displays selected records and derives the people directory from the credited names.

Run `node --check dist/app.js` and `node check-catalog.mjs` after editing.

## Bengaluru archive import

Official catalogue URLs for the 17 editions are in `tools/biffes-sources.json`, keyed by edition number. Convert downloaded catalogues to `1.txt` through `17.txt` with `pdftotext -layout`. The optional `4-ocr.txt` is the searchable text from Internet Archive item `unset0000unse_n1n9`. The optional `9-ocr.txt` is layout text from the searchable PDF linked on Internet Archive item `biffes.9th-biffes-catalogue-2017`. Run `python3 tools/import-biffes.py <text-directory> dist/catalog.json` to rebuild the extracted entries.

The importer adds printed page references for index-only entries and PDF page links for matching film pages. Scanned and irregular layouts can leave gaps. A PDF link in the edition selector indicates a source is available, even when no titles could be extracted from it. Portraits have source and license credits in their profile. Profiles without a sourced portrait use initials.
