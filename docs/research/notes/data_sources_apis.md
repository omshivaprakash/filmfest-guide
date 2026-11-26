# Data sources and APIs for a worldwide film festival guide

Research date: 2026-11-26. Test setup: a sandbox container behind an egress proxy. query.wikidata.org could be reached and was tested live. overpass-api.de, api.themoviedb.org and datasets.imdbws.com were all blocked by the proxy (HTTP 403 from the proxy, not from the services), so I could not test them. Their notes below come from documentation only.

## 1. Wikidata: data model and working SPARQL for festivals, editions and awards

### Takeaway
Wikidata is the best CC0 backbone for the guide. The live endpoint returned 16,177 festival items (instances of film festival Q220505 or its subclasses), 4,139 festival-edition items (class Q27787439) and several hundred award wins per major festival. Coverage is uneven. Only 653 festivals have direct coordinates, about half have a country, and only 917 editions have a start date. Expect to enrich the data from other sources.

### Cited Findings
- Licence: Wikidata data is CC0 ("No rights reserved"). Attribution is not required, but Wikidata asks to be credited as the source — [Wikidata:Data access](https://www.wikidata.org/wiki/Wikidata:Data_access)
- Access rules: send a good User-Agent header and `Accept-Encoding: gzip,deflate`, and do not send many requests at once. On HTTP 429, stop and honour `Retry-After`. Use dumps for very large result sets. Use the Wikibase REST API (still in development) for fetching individual entities, and Linked Data Fragments (experimental) for large triple-pattern results — [Wikidata:Data access](https://www.wikidata.org/wiki/Wikidata:Data_access)
- The Data access page gives no numeric WDQS limits. The widely documented limit is a 60-second query timeout, as reflected in client libraries such as [WikidataQueryServiceR docs](https://search.r-project.org/CRAN/packages/WikidataQueryServiceR/WikidataQueryServiceR.pdf). I did not verify the exact per-IP quotas on an official page; see Gaps.
- **Live test observations (2026-11-26, my own runs against https://query.wikidata.org/sparql):**
  - The festival list query (Q1 below) **ran in 7.5 s** and returned **16,577 rows / 16,177 distinct festivals**.
    - Distinct festivals with P17 country: **8,221**.
    - With P625 coordinates: **653**.
    - With P856 website: **14,263**.
    - With P571 inception: **2,292**.
  - Direct `wdt:P31 wd:Q220505` only: **15,988** items. The subclass path `wdt:P31/wdt:P279*` adds about 190 items.
  - Cannes (Q42369) is typed "annual film festival" / "recurring event" / "organization", not Q220505 directly. You need the `P279*` path to catch it.
  - Classes of items linked to festivals via P179/P361:
    - film festival edition **Q27787439**: 3,652
    - film award category Q56116950: 149
    - award ceremony Q4504495: 99
    - festival occurrence Q27968043: 91
    - recurring event edition Q27968055: 64
  - The editions query (Q2) **ran in 1.8 s**. It returned **4,139 distinct editions**:
    - 3,915 linked to a parent festival via P179/P361
    - only **917 with P580 start time**
  - Awards conferred via P1027 alone return few results for Cannes. Restricting awards to `P1027 = festival` gave Berlin 595, Venice 238 and **Cannes only 84** rows. The Palme d'Or (Q179808) has **no P1027**. It is typed `P31 = "Cannes Film Festival Awards"`, and 157 items have P166 = Palme d'Or.
  - The UNION pattern in Q3 fixes this. It returned Cannes **22 awards / 753 wins**, Berlin 22 / 617 and Venice 11 / 319.
  - Nominations: only **28** P1411 (nominated for) statements point to the Palme d'Or. Wikidata does not model competition line-ups well.
  - **Rate limiting seen live:** two back-to-back heavy queries produced **HTTP 429** (Wikimedia error page) for a few minutes. One exploratory query with `CONTAINS(LCASE(label))` over all labels hit the **60 s timeout (HTTP 504 "upstream request timeout")**.
- Key properties used:
  - P31 instance of, P279 subclass of
  - P17 country, P131 located in admin entity, P276 location, P625 coordinates
  - P571 inception, P856 official website
  - P179 part of the series, P361 part of
  - P580 / P582 start and end time, P585 point in time, P393 edition number
  - P1027 conferred by, P166 award received, P1411 nominated for
  - All of these were used successfully in the queries above (own test).

### Working SPARQL (all run successfully on 2026-11-26 unless noted)

Q1 — all film festivals with country, coordinates, website and inception (16,177 festivals, 7.5 s):
```sparql
SELECT ?fest ?festLabel ?countryLabel ?coord ?website ?inception WHERE {
  ?fest wdt:P31/wdt:P279* wd:Q220505 .
  OPTIONAL { ?fest wdt:P17 ?country . }
  OPTIONAL { ?fest wdt:P625 ?coord . }
  OPTIONAL { ?fest wdt:P856 ?website . }
  OPTIONAL { ?fest wdt:P571 ?inception . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,mul,fr,de,es". }
}
```
Suggested additions, not run in this exact form:
- Add `OPTIONAL { ?fest wdt:P131 ?admin . ?admin wdt:P625 ?adminCoord }` to fall back to the city's coordinates when the festival has none.
- Add `OPTIONAL { ?fest wdt:P18 ?image }` to get a Commons image.

Q2 — festival editions with dates (4,139 editions, 1.8 s):
```sparql
SELECT ?edition ?editionLabel ?festLabel ?start ?end WHERE {
  ?edition wdt:P31 wd:Q27787439 .
  OPTIONAL { ?edition wdt:P179|wdt:P361 ?fest . }
  OPTIONAL { ?edition wdt:P580 ?start . }
  OPTIONAL { ?edition wdt:P582 ?end . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,mul". }
}
```
For wider coverage, also include classes Q27968043 (festival occurrence) and Q27968055 (recurring event edition), and P585 (point in time).

Q3 — award winners by festival (UNION pattern; Cannes 753, Berlin 617, Venice 319 win statements):
```sparql
SELECT ?festLabel ?award ?awardLabel ?winner ?winnerLabel ?year WHERE {
  VALUES ?fest { wd:Q42369 wd:Q130871 wd:Q49024 }   # Cannes, Berlinale, Venice
  { ?award wdt:P1027 ?fest }
  UNION { ?award wdt:P31 ?cls . ?cls wdt:P1027|wdt:P361 ?fest }
  UNION { ?award wdt:P361 ?fest . ?award wdt:P31/wdt:P279* wd:Q618779 }
  ?winner p:P166 ?st . ?st ps:P166 ?award .
  OPTIONAL { ?st pq:P585 ?year . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,mul". }
} ORDER BY ?festLabel ?awardLabel DESC(?year)
```
The run that produced the counts used aggregation (COUNT DISTINCT). The simpler P1027-only version of the row query also ran, in 6.7 s with 917 rows.

Q4 — nominations (very sparse):
```sparql
SELECT ?film ?filmLabel ?year WHERE {
  ?film p:P1411 ?s . ?s ps:P1411 wd:Q179808 .
  OPTIONAL { ?s pq:P585 ?year }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". } }
```
This returned 28 rows.

### Inferences
- Use Wikidata QIDs as the guide's canonical IDs for festivals, films and people. They link to IMDb (P345), TMDB (P4947 film / P4985 person) and Commons. I did not query these ID properties in this session.
- Geocoding has to come from the city: use P131 → P625, or OSM/Nominatim.
- Edition dates are mostly missing, so the current year's dates must come from festival websites or the FIAPF calendar.
- About 14k festivals have P856 websites while only about 8k have a country. That ratio suggests a bulk import of thinly described festival items, so expect many low-quality or obscure entries. Filter them, for example by sitelinks count or presence of P17.
- Use a descriptive User-Agent, run queries one at a time, and back off on 429. A weekly cron with a few queries is well within normal use.

### Gaps
- I did not find an official page in this session stating the current WDQS numeric quotas. Known figures are a 60 s timeout and per-IP processing-time limits. I also did not verify the status of the 2025 WDQS graph split (main vs scholarly), which does not affect film data.
- I did not check how Q3 behaves when run for all festivals at once. Without the VALUES filter it may time out, so page it per festival.

## 2. Film and people APIs: TMDB, OMDb, IMDb datasets, Letterboxd, JustWatch

### Takeaway
TMDB is the most practical source for film and person metadata and images. It is free for non-commercial use with attribution, and commercial use needs a licence. The IMDb TSV dumps are daily but personal/non-commercial only. Letterboxd and JustWatch are partner-only. Check OMDb's licence before use; it was not verified here.

### Cited Findings
- **TMDB:**
  - Free for non-commercial use "as long as you attribute TMDB as the source". Commercial use requires a licence via sales.
  - Definition of commercial: "Your project is considered commercial if the primary purpose is to create revenue for the benefit of the owner."
  - Required notice: "This product uses the TMDB API but is not endorsed or certified by TMDB", shown in an About or Credits section. Use only approved, unmodified logos and the names "TMDB" or "The Movie Database".
  - Source: [TMDB developer FAQ](https://developer.themoviedb.org/docs/faq)
  - The full [API Terms of Use](https://www.themoviedb.org/api-terms-of-use) page could not be fetched (robots-disallowed), so I could not verify caching and rate-limit clauses.
- **IMDb non-commercial datasets:**
  - Files (gzipped UTF-8 TSV at https://datasets.imdbws.com/): title.akas, title.basics, title.crew, title.episode, title.principals, title.ratings, name.basics.
  - Refreshed daily.
  - "Available for access to customers for personal and non-commercial use", subject to IMDb terms.
  - Source: [IMDb Non-Commercial Datasets](https://data.imdb.com/non-commercial-datasets) (developer.imdb.com/non-commercial-datasets now redirects there)
  - The dumps contain **no festival or award data**. IMDb event pages exist (e.g. [Cannes ev0000147](https://www.imdb.com/event/ev0000147/2012)), but they are not in the datasets, and scraping is governed by IMDb [conditions of use](https://m.imdb.com/conditions).
- **Letterboxd:** API access goes through an application/beta page, [letterboxd.com/api-beta](https://letterboxd.com/api-beta/), with docs at [api-docs.letterboxd.com](https://api-docs.letterboxd.com). The page could not be fetched to confirm the current terms, so treat access as by request only.
- **JustWatch:** Partner-only. "Once the contract is concluded, each partner is handed a unique partner token." Partners must integrate branded links back to JustWatch — [JustWatch API docs](https://apis.justwatch.com/docs/api)
- **OMDb:** Only aggregator pages were found, e.g. [Zuplo comparison](https://zuplo.com/blog/2024/10/03/best-movie-api-imdb-vs-omdb-vs-tmdb). I could not verify the primary licence or limits (see Gaps).

### Inferences
- If the guide is non-commercial (e.g. a hobby site on GitHub Pages without ads), use TMDB for posters, synopses and credits, with attribution. Join via Wikidata P4947, or TMDB `/find/{imdb_id}?external_source=imdb_id`.
- Avoid shipping IMDb dump data in a public site if there is any revenue intent. Use only IMDb IDs as cross-reference keys.
- Do not rely on Letterboxd or JustWatch without a partnership. Link out to them instead.

### Gaps
- OMDb terms were not verified (omdbapi.com not fetched). From memory, there is a free key of about 1,000 requests/day, Patreon tiers, and CC BY-NC 4.0 data. This is unconfirmed.
- TMDB rate limits were not verified in this session. From memory, the old 40 requests per 10 s limit was removed in 2019 and an approximate 50 requests/s ceiling remains. This is unconfirmed.
- Neither TMDB nor IMDb could be live-tested because the hosts were blocked by the proxy.

## 3. Festival-specific sources: FIAPF, FilmFreeway, Festhome, Shortfilmdepot, Festival Scope, Cinando, Wikipedia, Kaggle/GitHub, Academy database

### Takeaway
No open, licensed, machine-readable worldwide festival directory exists. FIAPF publishes the authoritative list of accredited festivals, including a yearly calendar PDF. The submission platforms (FilmFreeway, Festhome, Shortfilmdepot) hold the biggest directories but offer no public directory API. Ready-made datasets exist only for the big events (Oscars, Cannes competition).

### Cited Findings
- **FIAPF:**
  - The accredited competitive feature film festivals page lists 14: Berlinale, Cairo, Fajr, Cannes, IFFI Goa, Karlovy Vary, Locarno, Mar del Plata, San Sebastián, Shanghai, Tallinn Black Nights, Tokyo, Venice, Warsaw — [FIAPF competitive feature film festivals](https://fiapf.org/festivals/accredited-festivals/competitive-feature-film-festivals/)
  - There is a separate competitive specialised category — [FIAPF specialised](https://fiapf.org/festivals/competitive-specialised-feature-film-festivals/)
  - A dated 2026 calendar PDF exists — [2026 Calendar FIAPF Accredited Festivals](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf)
  - Overview of the accreditation scheme — [FIAPF accreditation](https://fiapf.org/accreditation-program/)
  - Screen Daily reported a FIAPF revamp giving 17 festivals an official "A-list" classification — [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article). I saw only the headline; the article was not fetched.
  - The 14 on the competitive page versus 17 "A-list" may reflect different categories. This is unreconciled.
- **FilmFreeway:**
  - Has an API terms page, last updated 2026-08-13 — [FilmFreeway API ToS](https://filmfreeway.com/page/api-terms-of-service)
  - Help docs describe a **Submissions API** that festivals enable with an API key for their own submissions — [FilmFreeway help: Submissions API](https://filmfreeway.com/help/article/16110/add-an-api-key)
  - Neither the API ToS nor the main [terms of service](https://filmfreeway.com/page/terms-of-service) could be fetched (client error), so I could not quote the anti-scraping clauses.
  - Third-party scrapers exist (e.g. an [Apify festival actor](https://apify.com/versusmedia/festival-api-actor), a [morph.io scraper](https://api.morph.io/Malikplays/filmfreeway_festival_contacts)), which signals demand, not permission.
- **Festhome** has a public paginated festival list — [Festhome festival list](https://filmmakers.festhome.com/festival-list/page/page:124). I found no API or terms.
- **Shortfilmdepot / Festhome / FilmFreeway as a short-film market:** for industry context see [shortfilm.de on service providers](https://www.shortfilm.de/en/dienstleister-im-kurzfilmsektor-vertikale-integration-bei-online-anbietern/). Not fetched.
- **Kaggle/GitHub datasets:**
  - "The Oscar Award" Kaggle dataset (unanimad), mirrored at [Baselight](https://baselight.app/u/kaggle/dataset/unanimad_the_oscar_award)
  - Other Oscar datasets on Kaggle, e.g. [pushpakhinglaspure](https://baselight.app/u/kaggle/dataset/pushpakhinglaspure_oscar_dataset)
  - Zenodo records on festival and Oscar data: [Zenodo 4662041](https://zenodo.org/records/4662041), [Zenodo 4244742](https://zenodo.org/record/4244742). Contents not checked.
  - The Great Tables Python package ships a `films` dataset of **1,851 Cannes competition features from 1946 to present**. Columns: year, title, original_title, director, languages (ISO 639), countries_of_origin (ISO 3166), run_time, imdb_url — [great_tables.data.films](https://posit-dev.github.io/great-tables/reference/data.films.html)
- **Wikipedia:** list and records pages such as [List of Cannes Film Festival records](https://www.wikipedia.org/wiki/List_of_Cannes_Film_Festival_records) and the general [Film festival](https://www.wikipedia.com/wiki/Film_festival) article (CC BY-SA text). These need table parsing.

### Inferences
- Seed the "major festivals" tier from FIAPF plus Wikidata.
- Get each edition's current dates from the FIAPF calendar PDF (yearly manual or semi-automatic parse) and the festivals' own websites (P856).
- Treat FilmFreeway, Festhome and Shortfilmdepot as link-out targets, not data sources, unless a partnership is agreed.
- Wikipedia tables are CC BY-SA (share-alike). Data extracted into Wikidata is CC0, so prefer Wikidata.

### Gaps
- FilmFreeway, Letterboxd and TMDB terms pages could not be fetched, so the exact clauses are unverified.
- Not researched for lack of tool budget, and none were confirmed:
  - Festival Scope (industry screening platform)
  - Cinando (Marché du Film's paywalled industry database)
  - Shortfilmdepot's terms
  - the Academy Awards official database (awardsdatabase.oscars.org)
  - the "List of film festivals" Wikipedia page
  - Kaggle dataset licences
  - Eventival (festival management software, e.g. [eventival.com](https://eventival.com/?page_id=17))

## 4. Venues and cinemas: OSM Overpass, ODbL, Nominatim, Wikimedia Commons

### Takeaway
OpenStreetMap `amenity=cinema` is the open source for cinemas worldwide, under ODbL. The public Overpass servers are badly overloaded in 2026 and hard-ban IPs that exceed quotas. Use scheduled, low-volume queries, a self-hosted instance, or Geofabrik extracts. Nominatim is limited to 1 request per second, results must be cached, and bulk geocoding is discouraged.

### Cited Findings
- **overpass-api.de (FOSSGIS) limits:**
  - Under 10,000 queries/day, under 1 GB/day download, and under 10 minutes of total processing time per day.
  - For regular use, divide those limits by 100 (under 100 queries and under 10 MB per day).
  - Send a User-Agent or Referer, do not run scripts in parallel, and wait 30 s after HTTP 429/406.
  - Commercial use should go to self-hosted or paid servers.
  - The page says the main instance is overloaded. Alternatives include private.coffee, VK Maps, NextGIS (free key), Overpass.ch (10k requests/month) and paid Geofabrik.
  - Source: [OSM wiki: Overpass API](https://wiki.openstreetmap.org/wiki/Overpass_API)
- **Overpass performance in 2026:**
  - A community thread (posts from Sept to Nov 2026) reports servers "barely usable for over a year", 502 "at capacity" errors, and IPs hard-banned until quotas refill.
  - Load is attributed largely to AI agents and AI-generated apps.
  - Suggested alternatives: self-hosted dockerized Overpass, GeoDesk, Geofabrik extracts filtered with osmium and queried in DuckDB, and PMTiles.
  - Source: [OSM Community: Overpass API performance issues, p.10](https://community.openstreetmap.org/t/overpass-api-performance-issues/140598?page=10)
- **Nominatim policy:** "an absolute maximum of 1 request per second". Requires an identifying User-Agent or Referer ("stock User-Agents as set by http libraries will not do"). Requires visible attribution. "Results must be cached on your side." Bulk geocoding is "not encouraged". Autocomplete on the public API is forbidden — [Nominatim Usage Policy](https://operations.osmfoundation.org/policies/nominatim/)
- **Overpass test status:** NOT run. overpass-api.de, overpass.kumi.systems and overpass.private.coffee were all refused by the sandbox egress proxy. The queries below are untested.

Example Overpass QL (untested in this session):
```
[out:json][timeout:120];
area["ISO3166-1"="FR"][admin_level=2]->.a;
nwr["amenity"="cinema"](area.a);
out center tags;
```
Count only: replace the last line with `out count;`.

Around a festival city, using coordinates from Wikidata:
```
[out:json][timeout:60];
nwr["amenity"="cinema"](around:5000,43.5513,7.0128);
out center tags;
```
Useful tags: `name`, `website`, `wikidata`, `addr:*`, `screen`, `operator`.

### Inferences
- Cinemas are about a 100k-scale global set. Rather than running a global Overpass query, download Geofabrik country extracts in CI and filter them with `osmium tags-filter ... nwr/amenity=cinema`. This avoids public-server quotas entirely.
- Store the OSM element IDs and refresh weekly.
- ODbL requires attribution ("© OpenStreetMap contributors"). A derived *database* that is publicly distributed must be share-alike. Keep the cinema layer as a separate ODbL file in the repo.
- Use the OSM `wikidata=*` tag to join venues to Wikidata.

### Gaps
- The ODbL licence text and the OSMF attribution guidelines were not fetched in this session. These are standard facts, but this session gives no citation for them.
- Wikimedia Commons licensing (per-file CC BY / BY-SA / PD; use the Commons API `imageinfo&iiprop=extmetadata` for licence and author) was not researched in this session. This is unverified.

## 5. Map tiles and libraries for GitHub Pages without keys

### Takeaway
On a keyless static site, the safest options are:
- MapLibre GL JS with OpenFreeMap: free, no key, commercial use allowed, with OSM and OpenMapTiles attribution.
- A self-hosted Protomaps PMTiles file served from static hosting.

tile.openstreetmap.org is allowed for low-traffic Leaflet maps if you follow its policy, with no SLA. CARTO now requires an API key.

### Cited Findings
- **OSM tile policy (tile.openstreetmap.org):**
  - Attribution must be clearly visible on the map.
  - Send a unique User-Agent; browsers must send a valid Referer, so do not set a Referrer-Policy that strips it.
  - Do not bypass caches; cache tiles for at least 7 days if you cannot read the headers.
  - No bulk downloading, prefetching or offline use.
  - Access may be blocked without notice. "Availability is best-effort: there is no SLA."
  - Source: [OSMF Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/). A separate [OSMF Vector Tile Usage Policy](https://operations.osmfoundation.org/policies/vector/) also exists; not fetched.
- **OpenFreeMap:**
  - Public instance is "completely free", with no limits on views or requests.
  - No API key, registration or cookies. Commercial use allowed.
  - Attribution required: "© OpenMapTiles" and "Data from OpenStreetMap". MapLibre adds it automatically.
  - Styles: Positron, Bright, Liberty, Dark, Fiord, 3D.
  - MIT-licensed, self-hostable, with weekly planet downloads as MBTiles or PMTiles. No SLA.
  - Source: [openfreemap.org](https://openfreemap.org)
- **CARTO basemaps:**
  - Free only to customers "who request and use a CARTO-issued API key".
  - Fair-use caps: 5,000,000 tile requests/month for non-commercial use and 1,000,000/month for commercial use.
  - Free access is revocable. Attribution to both OSM and CARTO is required and must be "prominent and conspicuous".
  - Source: [CARTO Basemap Terms](https://www.carto.com/legal/basemap-terms/); [API key request](https://www.carto.com/basemaps/apikey/)
- **Protomaps/PMTiles:** a single-file tile archive served by HTTP range requests from static or CDN hosting, rendered with MapLibre. Docs: [Protomaps deploy docs](https://docs.protomaps.com/deploy/), [protomaps.com](https://protomaps.com/). Tutorials on hosting PMTiles on GitHub Pages: [dev.to guide](https://dev.to/ronitjadhav/how-to-host-and-test-pmtiles-on-github-pages-the-easiest-way-to-serve-maps-without-a-server-2ei8), [Simon Willison TIL](https://til.simonwillison.net/gis/pmtiles)

### Inferences
- Recommended setup: MapLibre GL JS plus the OpenFreeMap "positron" or "liberty" style URL, with a festival GeoJSON overlay. It needs no key and scales.
- Fallback: Leaflet plus OSM raster tiles, for low traffic only.
- For full independence, host a regional PMTiles extract. Be aware that GitHub Pages has a soft ~1 GB site limit, which is not verified here, and planet files are about 100 GB+. Use Cloudflare R2 or similar for large extracts.
- Avoid the old keyless CARTO URLs. The 2026 terms require a key.

### Gaps
- I did not confirm the exact OpenFreeMap style URL pattern (`https://tiles.openfreemap.org/styles/liberty` from memory).
- I did not verify Protomaps' hosted API key terms or the GitHub Pages size and bandwidth limits.

## 6. Calendar/ICS and schema.org markup for SEO

### Takeaway
Mark each festival edition up as a schema.org `Festival` (a subtype of Event) and each screening as a `ScreeningEvent` with `workPresented` → `Movie`. Google's Event rich-result requirements are `name`, `startDate` and `location` with an address. The Google page was updated 2026-09-08 with no deprecation notice.

### Cited Findings
- Google Event structured data:
  - Required: `name`, `startDate` (ISO 8601), `location` (Place with `address` as PostalAddress).
  - Recommended: `description`, `endDate`, `eventStatus`, `image` (16x9, 4x3 and 1x1), `location.name`, `offers`, `organizer`, `performer`, `previousStartDate`.
  - `eventStatus` values: EventScheduled, EventCancelled, EventPostponed, EventRescheduled. "When the event status changes, DON'T remove the startDate."
  - The page says it was last updated 2026-09-08 and has no deprecation notice.
  - Source: [Google Search Central: Event structured data](https://developers.google.com/structured-data/events/)
- schema.org types and properties: [Festival](https://schema.org/Festival), [Event](https://schema.org/Event), [workPresented](https://www.schema.org/workPresented) (used by ScreeningEvent to point at a Movie), [workFeatured](https://schema.org/workFeatured)

Example JSON-LD (illustrative):
```json
{"@context":"https://schema.org","@type":"Festival","name":"Festival de Cannes 2027",
 "startDate":"2027-05-11","endDate":"2027-05-22","eventStatus":"https://schema.org/EventScheduled",
 "location":{"@type":"Place","name":"Palais des Festivals","address":{"@type":"PostalAddress","addressLocality":"Cannes","addressCountry":"FR"}},
 "url":"https://www.festival-cannes.com/","sameAs":"https://www.wikidata.org/wiki/Q42369"}
```
The dates in this example are placeholders, not verified.

### Inferences
- Generate a per-festival `.ics` file plus an all-festivals `.ics` at build time. Each VEVENT needs DTSTART/DTEND as all-day `VALUE=DATE` with DTEND exclusive, plus a stable UID such as `<QID>-<year>@yourdomain`. Use the same data that generates the JSON-LD.

### Gaps
- RFC 5545 (iCalendar) was not fetched. The ICS details above come from general knowledge and are not cited.
- `eventAttendanceMode` (for online/hybrid festivals) is not on the Google page; check the schema.org Event page.

## 7. Keeping data fresh: GitHub Actions schedules and rate limits

### Takeaway
A scheduled GitHub Actions workflow that runs a few Wikidata queries and polite API calls, then commits JSON, fits every policy above. Two caveats: scheduled workflows in public repos are auto-disabled after 60 days without repo activity, and every service requires an identifying User-Agent and caching.

### Cited Findings
- GitHub disables scheduled workflows after 60 days of repository inactivity. Keepalive actions exist to prevent this — [gh-action-keepalive](https://github.com/efrecon/gh-action-keepalive); [keepalive-workflow](https://npmjs.com/package/keepalive-workflow); [HackerNoon: cron job can disappear](https://hackernoon.com/your-github-actions-cron-job-can-disappear-without-failing)
- The Overpass wiki tells users not to run Overpass from AI-generated app hosting platforms such as lovable.app or netlify.app, to identify themselves, and not to parallelise — [OSM wiki: Overpass API](https://wiki.openstreetmap.org/wiki/Overpass_API)
- Wikidata: on 429, back off per Retry-After; use dumps for very large pulls — [Wikidata:Data access](https://www.wikidata.org/wiki/Wikidata:Data_access)
- Nominatim: at most 1 request/s, single thread, cache results — [Nominatim policy](https://operations.osmfoundation.org/policies/nominatim/)
- IMDb datasets refresh daily — [IMDb datasets](https://data.imdb.com/non-commercial-datasets)

### Inferences
- Suggested cadence:
  - Weekly: Wikidata festivals, editions and awards (3–5 queries, run one after another with sleeps).
  - Monthly: OSM cinemas from Geofabrik extracts.
  - On demand: TMDB lookups, only for new QIDs. Cache by ID in the repo.
  - Yearly: manual pass on the FIAPF calendar PDF.
- Commit output as diffable JSON/CSV. Fail the job on large unexpected drops (e.g. more than 10% fewer festivals) to catch upstream breakage.
- Run a scheduled observation job: I saw 429s within a minute of back-to-back heavy queries, so serialise queries and add 5–10 s gaps.

### Gaps
- I did not fetch GitHub's official docs on the 60-day rule or on cron minimum interval and delay; only third-party sources are cited.
