# FilmFest Guide

A dependency-free festival archive, inspired by the [LitFest Speaker Guide](https://github.com/omshivaprakash/litfest-speaker-guide).

Run `python3 -m http.server 8000 --directory dist` from this folder and open http://localhost:8000.

Edit `dist/catalog.json` to extend the starter archive. Editions belong to festival IDs. Films link to an edition by festival ID and year. Each credit pairs a role with a name. Film awards can include a named recipient, and standalone awards can list a person without a film. Add source URLs alongside the claims they support. The archive displays selected records and derives the people directory from the credited names.

Run `node --check dist/app.js` and `node check-catalog.mjs` after editing.
