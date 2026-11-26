# Film Festival Ecosystem: Structure, Governance, Finance, Measurement and Research Data

Research date: 2026-11-26. About 25 tool calls. Some fetches failed (Screen Daily Venice 2026 feature); those topics are listed as gaps. "Background (not verified this session)" marks well-known facts I could not source in this session. The writer should treat them as unconfirmed.

## 1. FIAPF: what it is, accreditation categories and criteria, number of accredited festivals in 2026

### Takeaway
In 2026 FIAPF replaced its four-category system with one accredited list of 49 festivals in 29 countries. Within that list, 17 festivals carry a revived "A" classification based on reported data (submissions, industry attendance, press, audience figures).

### Cited Findings
- FIAPF represents 38 national producers' organisations from 31 countries. — [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article)
- The old four-category system was replaced by a single accredited list. The "A" classification returned about 20 years after it was dropped, for the festivals with the highest international impact. — [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article)
- New criteria:
  - Film selection: number of films submitted and share of non-native films entered.
  - Industry activity: professional attendees, journalists and press coverage.
  - Audience data: admissions, occupancy rates and audience development strategies.
  - Festivals supply the data voluntarily, and FIAPF publishes it on its website.
  - Source: [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article)
- 2026 list: 49 accredited festivals in 29 countries. — [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article); the [FIAPF 2026 calendar PDF (dated 2026-03-11)](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf) also lists 49.
- The 17 A-list festivals: Cannes, Berlin, Venice, Locarno, San Sebastián, Annecy, Clermont-Ferrand, Busan, Toronto, Mar del Plata, Shanghai, Cairo, IFFI Goa, Tokyo, Warsaw, Karlovy Vary and Tallinn Black Nights. — [FIAPF 2026 calendar](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf); [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article)
- The other 32 accredited festivals:
  - Santo Domingo Global, Bengaluru, Tampere, Málaga, Sofia, Punto de Vista, Hot Docs, Oberhausen
  - Kraków, Sydney, Transilvania, Cinema Jove, Golden Apricot Yerevan, Cinedays, Herceg Novi, Fantastic Fest
  - Eurasia, Festival du Nouveau Cinéma, Sitges, Rome, Viennale, Molodist Kyiv, Mostra de València, Kitzbühel
  - Kolkata, Antalya Golden Orange, Gijón, Zinebi Bilbao, Torino, Fajr, IFFK Kerala, Noir in Festival
  - Source: [FIAPF 2026 calendar](https://fiapf.org/wp-content/uploads/2026/03/2026_Calendar_FIAPF_Accredited_Festivals_20260311-2.pdf)
- Six festivals were newly accredited in 2026: Golden Apricot, Herceg Novi, FNC Montréal, Hot Docs, Annecy and Punto de Vista. Four more from under-represented regions were expected "later this year." — [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article)
- Data caveat: the Screen Daily article's table has 22 checkmarks in its A-list column, but the text names only 17. — [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article)

### Inferences
- A data model should store `fiapf_accredited` (boolean, per year) and `fiapf_a_list` (boolean, per year) as edition-level attributes, not fixed festival attributes. Accreditation changes from year to year.
- Sundance, SXSW, Tribeca, Rotterdam and Telluride are not on the FIAPF list. "A-list" in the press often means a status that differs from FIAPF's. The app should keep "FIAPF A-list" separate from informal "tier."
- Background (not verified this session): the old system ran from about the 2000s to 2025. It had four categories: competitive feature, competitive specialised, non-competitive and documentary/short. The best-known group was the "competitive feature" category of roughly 14–15 festivals.

### Gaps
- Whether the four expected additional festivals were accredited by November 2026. Not found.
- The exact year the "Revamp" article appeared. Undated; context suggests early 2026.

## 2. How many film festivals exist worldwide? Growth trends

### Takeaway
Credible estimates run from about 3,000 "active" festivals (Stephen Follows, 2013 data) to "more than 10,000" (St Andrews). The gap comes from definitions: ever-held versus active, and whether online or tiny events count. Most festivals are young, short and based in North America.

### Cited Findings
- Stephen Follows (article dated 2013-08-19):
  - 9,706 festivals had run at least once in the previous 15 years.
  - 2,954 were active, meaning they ran in the past two years.
  - The data combined 12 sources (Withoutabox, FilmFestivals.com, Festival Focus, BestInFest, British Council, Wikipedia, IMDb and others), with an estimated 90–95% accuracy.
  - Source: [Stephen Follows](https://stephenfollows.com/many-film-festivals-are-in-the-world/)
- Growth and age (2013 data):
  - About 75% of festivals were created in the previous ten years, and half since 2008.
  - 2011 was the peak year for new festivals. Launches fell almost a fifth in 2012.
  - About 39% ran only once, and fewer than a quarter were more than six years old.
  - Source: [Stephen Follows](https://stephenfollows.com/many-film-festivals-are-in-the-world/)
- Geography and format (2013 data):
  - About 70% are in North America.
  - 77% screen shorts and 52% screen features.
  - About half have a competition, and half run fewer than 7 days.
  - October is the busiest month, with about five times as many festivals as December.
  - Source: [Stephen Follows](https://stephenfollows.com/many-film-festivals-are-in-the-world/)
- What directories claimed then (2013): Withoutabox ">5,000" (850–900 open for entries); FilmFestivals.com 4,000–6,000; Festival Focus 2,303; BestInFest 1,832; British Council 1,582; Wikipedia list 437. — [Stephen Follows](https://stephenfollows.com/many-film-festivals-are-in-the-world/)
- The University of St Andrews (Dina Iordanova's project) says "there are more than 10,000 festivals… and the number is still rising." It dates the first festival to Venice, 1932. — [St Andrews](https://www.st-andrews.ac.uk/film-studies/research/impact/film-festivals/)

### Inferences
- The app should not present a single number. "About 3,000 active, 10,000+ ever held" is a defensible range, with both dates shown.
- The modern equivalent of Withoutabox (closed in 2019) is FilmFreeway. Its listed count would be the best current proxy, but I did not get a figure (see Gaps).

### Gaps
- A FilmFreeway festival count for 2025–2026. No reliable figure found. Commonly quoted "10,000+ festivals on FilmFreeway" claims could not be verified.
- No post-2020 academic census of festival numbers was found, and no data on net closures after COVID.

## 3. Festival economics: budgets, public funding, economic impact, attendance

### Takeaway
Large festivals cost tens of millions and rely heavily on public money. The Berlinale has a budget of about €33M, with €11.9M in federal funding for 2026. Economic impact studies, usually commissioned by the festivals, claim $200M–$240M for Sundance and TIFF.

### Cited Findings
- **Berlinale**:
  - Budget of about €33M; staff costs over €12M.
  - BKM (federal) funding of €11.9M for 2026. Berlin Senate funding of €1M.
  - Director Tricia Tuttle warned of a budget gap and likely cuts in 2027–2028.
  - Source: [Screen Daily](https://www.screendaily.com/news/berlinale-facing-funding-shortfall-in-2027-and-2028-warns-festival-director/5213254.article)
- **Berlinale federal grant history**:
  - Raised from €10.9M to €12.9M in 2025 (under Claudia Roth), then cut to €11.9M for 2026 (under Wolfram Weimer).
  - The Berlinale earns 60% of its budget itself. Sponsorship rose 27% in 2025.
  - The 2026 edition showed 218 films (55 German productions or co-productions) and was described as the festival with the largest audience worldwide.
  - Source: [Bundestag hib 34/2026, 2026-01-14](https://www.bundestag.de/presse/hib/kurzmeldungen-1136674)
- **Sundance 2025** (the second-to-last Park City edition):
  - More than 85,000 attendees, up 17% from 2024 but down almost 40% from 2020 in-person attendance.
  - About a third of visitors came from out of state.
  - Nearly $200M of economic impact for Utah and over 2,600 jobs, according to the festival's commissioned report.
  - Source: [KPCW, 2025-09-02](https://www.kpcw.org/park-city/2025-09-02/report-sundance-attendance-jumps-17-at-2025-festival); [Sundance 2025 Economic Impact Report PDF](https://www.sundance.org/wp-content/uploads/2025/07/2025-Sundance-Film-Festival-Attendance-Recap-and-Economic-Impact-Report.pdf)
- **TIFF** (2024 figures): $240M in economic activity, $36M a year in tax revenue for all levels of government, more than 700,000 visitors over 11 days, and 291 films. — [The Varsity, 2025-09-14](https://thevarsity.ca/2025/09/14/how-tiff-powers-torontos-economy/). An older Ontario Creates impact report is also available: [TIFF Final Report, Oct 2019](https://www.ontariocreates.ca/uploads/Business_Intelligence/en/TIFF_Final_Report_October_2019.pdf). A Visa "TIFF50 economic effects" document exists but I did not read it: [Visa PDF](https://corporate.visa.com/content/dam/VCOM/corporate/services/documents/tiff50-economic-effects.pdf).
- TIFF 2026 ticket price increases caused "people's festival no more" complaints. — [CP24, 2026-08-31](https://www.cp24.com/local/toronto/2026/08/31/peoples-festival-no-more-tiff-fans-grapple-with-ticket-price-hikes/)
- **Cannes / Marché du Film 2026**:
  - About 40,000 accredited professionals at the festival.
  - About 16,000 Marché participants from more than 140 countries, up from 15,000+ in 2025.
  - 1,700 buyers, 600 exhibiting companies, 1,500 screenings, 250 industry events.
  - Source: [Marché du Film](https://www.marchedufilm.com/news/the-marche-du-film-maintains-record-levels-of-participation-and-confirms-its-global-leadership/); [Stephen Follows](https://stephenfollows.com/p/nine-takeaways-from-the-2026-cannes-marche-du-film)
- **EFM 2026 (Berlin)**:
  - More than 12,500 professionals, up 5%.
  - 1,794 buyers and 606 films, with an 83.17% market-premiere rate.
  - More than 100 sessions with 369 speakers.
  - Source: [Berlinale press release](https://www.berlinale.de/en/2026/news-press-releases/277528.html). A trade commentary called it "attendance up, deals down": [Filmtake](https://www.filmtake.com/?p=43470)
- Stephen Follows also published an analysis of TIFF's costs and income (date not checked). — [Stephen Follows](https://stephenfollows.com/costs-income-films-toronto-international-film-festival)

### Inferences
- Economic-impact figures are commissioned by the festivals and use different methods (gross spending versus net new spending). The app should label them as "festival-reported" and not rank festivals by them.
- Useful statistics fields: `budget_total`, `public_funding` (with a source level of federal, regional or city), `admissions`, `accredited_professionals`, `market_participants`, `buyers`, `films_screened`, and `economic_impact_reported` with `study_author`.

### Gaps
- Cannes festival budget (often quoted at about €20M+ with about half public money). Not verified this session.
- Venice/Biennale budget, and Berlinale 2026 ticket and admission totals (historically about 330,000 tickets). Not verified.
- Sundance 2026 attendance and the details of Colorado's incentive package. Not found in the fetched sources.
- TIFF 2025 and 2026 economic figures, and the budget from its charity filings ([Charity Intelligence profile](https://charityintelligence.ca/charity-details/336-toronto-international-film-festival), not read).

## 4. Gender and diversity in line-ups and juries

### Takeaway
Women remain a minority in the top competitions. Cannes 2026 had 5 of 22 competition films directed by women (down from 7 of 22 in 2025), and Venice 2026 had 2. Festivals point to higher shares in their wider official selections.

### Cited Findings
- **Cannes 2026**:
  - 5 of 22 Palme d'Or contenders were directed by women (about 23%), compared with 7 of 22 in 2025 (about 32%).
  - Organisers said women directed 34% of all features in the official programme, or 38% including shorts.
  - Only three women have won the Palme d'Or. The most recent was Justine Triet in 2023 (*Anatomy of a Fall*).
  - Source: [CP24/AFP, 2026-05-11](https://www.cp24.com/news/entertainment/2026/05/11/cannes-film-festival-defends-male-dominated-competition/)
- Thierry Frémaux rejected quotas ("Under no circumstances should there be a quota policy"). He said that between a male and a female director's film of equal merit, "we will choose the film by the female director." Collectif 50/50 accused Cannes of "feminism washing" over its *Thelma & Louise* poster. — [CP24](https://www.cp24.com/news/entertainment/2026/05/11/cannes-film-festival-defends-male-dominated-competition/)
- **Venice 2026**: 2 female-directed competition films. Jury president Maggie Gyllenhaal called this "a systemic problem" and said "It's much harder for women to get their films financed" (2026-09-02). — [TheWrap](https://www.thewrap.com/creative-content/movies/maggie-gyllenhaal-female-directors-venice/)
- **Venice 2026, conflicting reports**: World of Reel headlined a Venice chief saying there was "one female director in competition… the only one we found of adequate quality." — [World of Reel, 2026-07-23](https://www.worldofreel.com/blog/2026/7/23/venice-film-festival-chief-on-one-female-director-in-competition-shes-the-only-one-we-found-of-adequate-quality). Screen's line-up analysis was headlined "studios and female directors go missing." — [Screen Daily](https://www.screendaily.com/features/six-talking-points-from-the-venice-2026-lineup-studios-and-female-directors-go-missing/5218857.article) (fetch failed). TheWrap's count of 2 may include a later addition, or the counts may differ. This is unresolved.

### Inferences
- Gender statistics need a `gender` attribute on Person (self-identified, nullable) and a link from director credits to film. Shares should be computed per section, because competition and full-selection shares differ a lot.
- Jury composition statistics follow the same pattern: jury membership linked to Person.

### Gaps
- A Cannes and Venice female-director series by year (for example 2010–2026). Not compiled this session. Collectif 50/50 and Women and Hollywood publish these, but I did not fetch them.
- Jury gender statistics, and race and ethnicity data. No sources fetched.
- Berlinale 2026 gender figures. Not found.

## 5. Festival strategy and circuit: premieres, tiers, sales agents, markets, co-production forums and funds

### Takeaway
Markets attached to festivals (the Marché du Film at Cannes, EFM at Berlin) are where sales happen, and both reported record or rising attendance in 2026 alongside cautious dealmaking. Premiere-status rules and the funds landscape are standard industry knowledge, but I could not source them this session.

### Cited Findings
- EFM reported an 83.17% "market premiere" rate across 606 films in 2026. Premiere status is a key metric even for markets. — [Berlinale](https://www.berlinale.de/en/2026/news-press-releases/277528.html)
- Marché du Film 2026 had strong Latin American representation, including activities with Ventana Sur. Japan, as Country of Honour, saw about +50% attendance, and a Japan IP Market launched. — [Marché du Film](https://www.marchedufilm.com/news/the-marche-du-film-maintains-record-levels-of-participation-and-confirms-its-global-leadership/); [Stephen Follows](https://stephenfollows.com/p/nine-takeaways-from-the-2026-cannes-marche-du-film)
- Market mood in 2026:
  - Fewer, more deliberate meetings.
  - Private equity filling gaps left by weaker pre-sales.
  - For the first time since 2017, no major studio brought a tentpole to Cannes.
  - Source: [Stephen Follows](https://stephenfollows.com/p/nine-takeaways-from-the-2026-cannes-marche-du-film)
- TIFF is promoting a 2026 content market, and sales agents are debating its ideal dates. — [Screen Daily](https://www.screendaily.com/news/tiff-touts-2026-content-market-as-sales-agents-mull-ideal-dates/5197040.article) (headline only). The 2026 TIFF trade expansion: [BizBash](https://www.bizbash.com/programming-entertainment/how-the-2026-toronto-international-film-festival-expanded-its-trade-presence) (not read).

### Inferences
Background, not verified this session. These are standard industry facts the writer should confirm before publishing.

- **Premiere hierarchy**:
  - World premiere: first public screening anywhere.
  - International premiere: first outside the country of production.
  - Then continental or regional (e.g. European, North American), national and city premieres.
  - FIAPF has historically required its top competitive festivals to show world or international premieres in competition.
- **Markets and their timing**:
  - Marché du Film (Cannes, May) and EFM (Berlin, February).
  - AFM (American Film Market, Santa Monica until 2024, then Las Vegas, November).
  - Ventana Sur (Buenos Aires, December, run with the Marché du Film).
  - Film Bazaar (Goa, alongside IFFI, November).
  - Asian Contents & Film Market (Busan, October).
- **Funds and labs**:
  - Hubert Bals Fund (IFFR Rotterdam)
  - World Cinema Fund (Berlinale)
  - Sundance Institute labs and grants
  - TorinoFilmLab (Torino)
- **Data model**: Premiere status should be an enum on the film-at-edition (Selection) record: world / international / continental / national / regional / local / none. It should not be an attribute of the Film.

### Gaps
- No fetched source gives formal premiere-status rules (FIAPF regulations), fund budgets or recipient counts, or 2026 AFM, Ventana Sur, Film Bazaar or ACFM attendance. All need follow-up.
- Sales agents: no sourced data on their number or market share.

## 6. Typical data model and existing schemas

### Takeaway
schema.org offers `ScreeningEvent` (with `workPresented` linking to `Movie`, and `superEvent`/`subEvent` for nesting a screening inside a festival). It is enough for publishing screenings but has no dedicated Festival, Award or Jury types. A richer internal model is needed.

### Cited Findings
- `schema.org/ScreeningEvent`:
  - Specific properties: `workPresented` (a Movie), `videoFormat` (e.g. IMAX, 3D) and `subtitleLanguage` (BCP 47).
  - Useful inherited Event properties: `superEvent`/`subEvent`, `location` (Place or VirtualLocation), `startDate`/`endDate`, `organizer`, `performer`, `director`, `eventStatus`, `eventAttendanceMode` (for online or hybrid editions) and `previousStartDate` (for reschedules).
  - Source: [schema.org](https://schema.org/ScreeningEvent)

### Inferences
- **Proposed entities** (my synthesis; field names are suggestions):
  - `Festival`: id, name, city, country, founded_year, organiser, FIAPF status by year, website, Wikidata QID.
  - `Edition`: festival_id, number, year, start and end dates, mode (in-person / hybrid / online), budget, admissions, cancelled flag.
  - `Section`: edition_id, name, competitive (boolean), type (main competition, sidebar, shorts, market).
  - `Film`: title, original title, year, countries, runtime, IMDb and Wikidata ids.
  - `Selection`: film × section, with premiere_status.
  - `Screening`: selection × venue × datetime, format, subtitle language, ticketing URL.
  - `Venue`: name, address, geo coordinates, capacity, screens.
  - `Person`: name, gender (nullable, self-identified), nationality, ids.
  - `Credit`: person × film × role, where role is director, producer, cast and so on.
  - `Jury`: edition × section.
  - `JuryMember`: jury × person × role (president or member).
  - `Award`: edition × name × category.
  - `Nomination` / `Prize`: award × film and/or person, with won (boolean) and ex-aequo flags.
  - `Market`, `CoproForum` and `Fund` as optional extensions.
- Map `Edition` and `Screening` to schema.org `Festival`/`Event` and `ScreeningEvent` in JSON-LD for SEO. Store Wikidata QIDs for deduplication.
- Background (not verified this session): Wikidata models festivals as "film festival" (Q220505) instances. Editions are separate items linked by "edition of" / "instance of". Awards use "award received" (P166) with qualifiers for "point in time" and "for work". Nominations use P1411.

### Gaps
- Wikidata property and class IDs were not checked live. Verify them before implementation.
- No open festival archive schema (for example from Cannes, Berlinale or IMDb event pages) was found or reviewed.

## 7. Academic research, books and journals

### Takeaway
Film festival studies became an established field from about 2007. It is anchored by Marijke de Valck's work, Skadi Loist's Film Festival Research Network (FFRN) bibliography, and Dina Iordanova's St Andrews project and *Film Festival Yearbook* series.

### Cited Findings
- FFRN thematic bibliography by de Valck and Loist (University of Amsterdam), with updates in 2009 and 2011. — [UvA DARE 2009](https://dare.uva.nl/id/b5fa90c1-d3e4-4228-9fd5-be7cec57c78c); [UvA DARE 2011](https://dare.uva.nl/id/afc9e635-cee1-405e-9c68-8cd7d4397903)
- de Valck and Loist, "Film Festival Studies: An Overview of a Burgeoning Field." — [PDF](https://is.muni.cz/el/phil/podzim2012/FAVz032/37474845/De_Valck__Marijke__and_Skadi_Loist_Film_Festival_Studies_An_Overview_of_a_Burgeoning_Field.pdf?lang=en)
- de Valck, Kredell and Loist (eds.), *Film Festivals: History, Theory, Method, Practice* (Routledge). — [Routledge](https://www.routledge.com/Film-Festivals-History-Theory-Method-Practice/de-Valck-Kredell-Loist/p/book/9780415712477)
- St Andrews film festival research, led by Prof. Dina Iordanova since 2008. It runs the *Film Festival Yearbook* series and works with festivals including Busan, Fajr, Singapore, Yala and Yamagata. — [St Andrews](https://www.st-andrews.ac.uk/film-studies/research/impact/film-festivals/); publications list: [Dynamics of World Cinema](https://st-andrews.ac.uk/~worldcin/index.php/publications.html)
- St Andrews news story "Around the world in 2000 film festivals." — [St Andrews news](https://news.st-andrews.ac.uk/?p=17257) (not read)

### Inferences
- Background (not verified this session):
  - de Valck, *Film Festivals: From European Geopolitics to Global Cinephilia* (Amsterdam University Press, 2007).
  - The *Film Festival Yearbook* series (St Andrews Film Studies, from 2009) has 6 volumes, covering the festival circuit, audiences, film financing, rights, activism, and Asia/Middle East.
  - Relevant journals: *NECSUS*, *Screen*, *Cinéaste*, and since 2023 the dedicated open-access journal *Film Festival Studies*.
  - filmfestivalresearch.org hosts the current FFRN bibliography.

### Gaps
- I did not reach filmfestivalresearch.org this session. The current bibliography size and the details of the *Film Festival Studies* journal are unverified.

## 8. Notable 2025–2026 trends

### Takeaway
The main trends:

- Sundance left Park City after its January 2026 edition for Boulder (January 21–31, 2027).
- Public funding is tightening (the Berlinale cut).
- Generative-AI policies are spreading.
- Studios and streamers are pulling back from Cannes.
- Female representation in major competitions remains low and contested.

### Cited Findings
- **Sundance relocation**:
  - Announced in March 2025. Park City hosted its final edition in January 2026.
  - The 2027 Boulder edition runs January 21–31, 2027, across 11 screening venues, including the Boulder Theater, Macky Auditorium (CU Boulder), Chautauqua Auditorium and Cinemark Century Boulder.
  - The festival was founded in 1985.
  - Source: [Variety AU](https://au.variety.com/2026/film/global/sundance-film-festival-2027-dates-boulder-colorado-33520/); [Axios Denver, 2025-03-27](https://www.axios.com/local/denver/2025/03/27/boulder-sundance-film-festival-2027); [Boulder city FAQ](https://bouldercolorado.gov/sundance-film-festival-frequently-asked-questions)
- **Funding pressure**: Berlinale federal grant cut from €12.9M to €11.9M, with cuts flagged for 2027–2028. — [Bundestag](https://www.bundestag.de/presse/hib/kurzmeldungen-1136674); [Screen Daily](https://www.screendaily.com/news/berlinale-facing-funding-shortfall-in-2027-and-2028-warns-festival-director/5213254.article)
- **AI policies**: Cinema St. Louis will bar generative-AI films from the St. Louis International Film Festival and its Filmmakers Showcase from 2027. Other AI uses and digital editing stay allowed. — [St. Louis Public Radio, 2026-09-08](https://www.stlpr.org/text/arts/2026-09-08/cinema-st-louis-limits-ai-use-festival-films)
- **Unconfirmed**: a blog claims Cannes 2026 banned generative AI from the Official Competition. — [aifilms.ai blog](https://studio.aifilms.ai/blog/cannes-2026-ai-ban-official-selection). This is a low-quality source; verify against Cannes regulations.
- **AI at markets**: Cannes 2026 had an AI for Talent Summit and a Creator Economy Summit. Soderbergh's *John Lennon: The Last Interview* uses Meta-generated video for about 10% of its runtime. About 4,000 French actors signed an anti-AI letter. — [Stephen Follows](https://stephenfollows.com/p/nine-takeaways-from-the-2026-cannes-marche-du-film)
- **Studios and streamers absent**: no major-studio tentpole at Cannes 2026, the first time since 2017. Screen Daily also flagged that studios were missing from Venice 2026. — [Stephen Follows](https://stephenfollows.com/p/nine-takeaways-from-the-2026-cannes-marche-du-film); [Screen Daily headline](https://www.screendaily.com/features/six-talking-points-from-the-venice-2026-lineup-studios-and-female-directors-go-missing/5218857.article)
- **Accreditation reform**: FIAPF's data-driven A-list revamp, covered in section 1. — [Screen Daily](https://www.screendaily.com/news/17-film-festivals-receive-official-a-list-classification-as-part-of-major-fiapf-revamp/5214719.article)

### Inferences
- The app should support an edition `mode` (in-person / hybrid / online) and a `status` (scheduled / cancelled / postponed), matching schema.org `eventStatus` and `eventAttendanceMode`. It should also handle a festival changing location between editions (Sundance), so location belongs to the Edition, not the Festival.

### Gaps
- A sourced list of festival closures or cancellations in 2025–2026. Not found this session.
- Hybrid and online edition statistics after COVID, and streaming-premiere counts (for example Netflix titles at Venice and TIFF 2026). Not researched.
