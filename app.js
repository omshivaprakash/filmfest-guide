const byId = id => document.getElementById(id);
const search = byId('search');
const edition = byId('edition');
const facet = byId('facet');
const kind = byId('kind');
const detail = byId('detail');
const content = byId('detail-content');
const results = byId('results');
// Same tab layout as LitFest Guide: a festival opens on Discover; "All" opens the home page.
const festivalTabs = { discover: 'Discover', films: 'Films', people: 'People', awards: 'Awards', map: 'Map', years: 'Past years' };
const searchTabs = { films: 'Films', people: 'People', awards: 'Awards' };
// Explore, like LitFest's: maps and research views across every festival.
const exploreTabs = { map: 'Map', calendar: 'Calendar', languages: 'Languages', roles: 'Roles', impact: 'Award impact', across: 'Across festivals', world: 'World festivals' };
const ROLES = ['Director', 'Writer', 'Actor', 'Producer', 'Cinematographer', 'Editor', 'Composer', 'Sound'];
const listViews = ['films', 'people', 'awards', 'years', 'across', 'world'];
const exploreViews = ['map', 'languages', 'roles', 'impact'];
const UNLISTED = 'Format unlisted';
let festivalId = '';
let view = 'home';

function element(tag, text, className) {
  const node = document.createElement(tag);
  if (text) node.textContent = text;
  if (className) node.className = className;
  return node;
}
function button(text, className, action) {
  const node = element('button', text, className);
  node.type = 'button';
  node.addEventListener('click', action);
  return node;
}
function source(url, label) {
  const link = element('a', label, 'source');
  link.href = url;
  link.target = '_blank';
  link.rel = 'noopener';
  return link;
}
function options(select, values, defaultLabel) {
  const previous = select.value;
  select.replaceChildren(new Option(defaultLabel, ''), ...values.map(([value, label]) => new Option(label, value)));
  if (values.some(([value]) => String(value) === previous)) select.value = previous;
}
const unique = values => [...new Set(values)];
const normalize = value => value.normalize('NFD').replace(/\p{Diacritic}/gu, '').toLowerCase();
const number = value => value.toLocaleString('en-IN');
const SMALL = new Set(['a', 'an', 'and', 'as', 'at', 'by', 'for', 'in', 'of', 'on', 'or', 'the', 'to', 'with']);
// Catalogue scans print many titles in capitals; show them in title case so lists read evenly.
function tidyTitle(title) {
  if (title !== title.toUpperCase() || !/\p{Lu}/u.test(title)) return title;
  return title.toLowerCase().replace(/[\p{L}\p{N}'’]+/gu, (word, offset) => {
    if (/^[ivxlc]+$/.test(word) && word.length > 1) return word.toUpperCase();
    if (offset > 0 && SMALL.has(word)) return word;
    return word[0].toUpperCase() + word.slice(1);
  });
}
function thumbnail(fallback, photo, className = 'thumbnail') {
  const frame = element('span', fallback, className);
  frame.setAttribute('aria-hidden', 'true');
  if (photo) {
    const img = element('img');
    img.alt = '';
    img.loading = 'lazy';
    img.src = photo.file;
    img.addEventListener('error', () => img.remove(), { once: true });
    frame.append(img);
  }
  return frame;
}
const initials = name => name.split(/\s+/).slice(0, 2).map(part => part[0]).join('');

async function start() {
  const linksLoad = fetch('data/youtube-links/youtube.json').then(reply => (reply.ok ? reply.json() : { films: {} })).catch(() => ({ films: {} }));
  const optional = url => fetch(url).then(reply => (reply.ok ? reply.json() : null)).catch(() => null);
  const extrasLoad = optional('data/enrich/films.json');
  const response = await fetch('catalog.json');
  if (!response.ok) throw new Error('Catalogue unavailable');
  const { festivals, films, honors, portraits = {}, worldFestivals: allHand = [] } = await response.json();
  // Extractor shards (data/<name>/catalog.json, listed in data/shards.json) add festivals, films and honours; a missing shard is skipped.
  const shardList = await fetch('data/shards.json').then(reply => (reply.ok ? reply.json() : [])).catch(() => []);
  for (const shard of await Promise.all(shardList.map(path => fetch(path).then(reply => (reply.ok ? reply.json() : null)).catch(() => null)))) {
    if (!shard) continue;
    festivals.push(...(shard.festivals || []));
    films.push(...(shard.films || []));
    honors.push(...(shard.honors || []));
    Object.assign(portraits, shard.portraits);
  }
  const imported = new Set(festivals.flatMap(record => [record.id, record.wikidata]).filter(Boolean));
  const handWorld = allHand.filter(record => !imported.has(record.id));
  const links = (await linksLoad).films;
  for (const film of films) {
    film.title = tidyTitle(film.title);
    Object.assign(film, links[film.id]);  // YouTube links and Wikidata ids from the youtube-links extractor
  }
  // Runtime, genres, IMDb id and Commons posters from the enrich extractor; the page works without it.
  const filmExtras = (await extrasLoad)?.films || {};
  for (const film of films) {
    const { poster, ...extra } = filmExtras[film.id] || {};
    Object.assign(film, { ...extra, ...film });
    if (poster && !film.artwork) film.artwork = poster;
  }
  const festivalMap = new Map(festivals.map(record => [record.id, record]));
  const label = record => `${festivalMap.get(record.festival).short} · ${record.year}`;
  const awards = films.flatMap(film => film.awards.map(award => ({ ...film, award, film }))).concat(honors);
  const people = new Map();
  const addCredit = (name, record) => {
    if (!people.has(name)) people.set(name, []);
    people.get(name).push(record);
  };
  for (const film of films) for (const [role, name] of film.credits) addCredit(name, { ...film, role, film });
  for (const honor of honors) addCredit(honor.award[2], honor);
  const countriesOf = film => (film.country ? film.country.split(', ') : []);
  const languagesOf = film => (film.language ? film.language.split(/\s*,\s*/) : []).filter(Boolean);
  let worldFestivals = handWorld;
  let regions = unique(worldFestivals.map(record => record.region));
  // The world list is large, so it loads after the first screen and is merged with the hand-checked entries.
  Promise.all([optional('data/world-festivals/world-festivals.json'), optional('data/enrich/festivals.json')]).then(([data, extras]) => {
    if (!data) return;
    for (const record of data.festivals) Object.assign(record, { ...extras?.festivals?.[record.id], ...record });
    const key = name => normalize(name).replace(/[^a-z0-9]/g, '');
    const host = url => { try { return new URL(url).hostname.replace(/^www\./, ''); } catch { return ''; } };
    const rows = data.festivals.filter(record => !imported.has(record.id)).map(({ ll, ...record }) => ({ ...record, lon: ll[0], lat: ll[1] }));
    const byName = new Map(rows.map(record => [key(record.name), record]));
    const byHost = new Map(rows.filter(record => record.url).map(record => [host(record.url), record]));
    const extra = [];
    for (const hand of handWorld) {
      const found = byName.get(key(hand.name)) || byHost.get(host(hand.url));
      if (found) Object.assign(found, { short: hand.short, month: hand.month, city: found.city || hand.city });
      else extra.push(hand);
    }
    worldFestivals = [...extra, ...rows].sort((a, b) => (b.links || 0) - (a.links || 0));
    regions = unique(worldFestivals.map(record => record.region)).sort();
    if (['home', 'world', 'map', 'calendar'].includes(view)) render();
  }).catch(error => console.warn('World festivals unavailable', error));
  const allRoles = unique([...people.values()].flat().map(record => record.role)).sort();
  const ON_YOUTUBE = 'On YouTube';
  const formats = [...unique(films.map(film => film.format)).filter(format => format !== UNLISTED).sort(), ON_YOUTUBE];
  const orderedFilms = [...films].sort((a, b) => Number(Boolean(b.artwork)) - Number(Boolean(a.artwork)));
  const filmsIn = (id, year) => films.filter(film => film.festival === id && (!year || film.year === year));
  const editionLabel = event => [event.number && `${event.number} edition`, [event.dates, event.year].filter(Boolean).join(' ')].filter(Boolean).join(' · ');
  // Calendar (calendar.js): guide festivals by their edition dates, world festivals by their usual month.
  const handMonth = new Map(allHand.map(record => [record.id, record.month]));
  let calendar;
  function calendarEntries() {
    if (calendar?.from !== worldFestivals) calendar = { from: worldFestivals, entries: [
      ...festivals.map(record => ({ record, guide: true, when: festivalWhen({ month: handMonth.get(record.id), ...record }) })),
      ...worldFestivals.map(record => ({ record, when: festivalWhen(record) }))
    ].filter(entry => entry.when) };
    return calendar.entries;
  }
  const whenOf = record => calendarEntries().find(entry => entry.record === record)?.when;
  const whenBadge = when => element('span', when.text, `when ${when.status}`);
  const openEntry = entry => (entry.guide ? go(entry.record.id, 'discover') : showWorld(entry.record));
  function whenChip(entry) {
    const chip = button('', `wchip ${entry.when.status}`, () => openEntry(entry));
    chip.append(element('b', entry.record.short || entry.record.name), element('span', entry.when.brief));
    chip.title = `${entry.record.name} · ${entry.when.text}`;
    return chip;
  }
  const onNow = () => calendarEntries().filter(entry => ['now', 'month'].includes(entry.when.status)).sort((a, b) => b.when.sure - a.when.sure || Boolean(b.guide) - Boolean(a.guide));
  const comingNext = () => calendarEntries().filter(entry => entry.when.status === 'next').sort((a, b) => a.when.start - b.when.start || Boolean(b.guide) - Boolean(a.guide));
  function renderCalendar() {
    const today = new Date();
    byId('cal-sub').textContent = `As of ${today.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' })}. Exact dates come from announced editions. “Usually” and “dates TBC” mean only the usual month is known, from past editions or Wikidata, so check the festival’s site before you travel.`;
    const recent = calendarEntries().filter(entry => entry.when.status === 'over' && today - entry.when.end < 45 * 864e5).sort((a, b) => b.when.end - a.when.end);
    const strip = (heading, entries, empty) => panel(heading, ...(entries.length ? [element('div', '', 'wchips')] : [element('p', empty, 'meta')]));
    const summary = [['Happening now', onNow(), 'Nothing on record for today.'], ['Coming next', comingNext(), 'Nothing on record yet.'], ['Just finished', recent, 'Nothing in the last six weeks.']].map(([heading, entries, empty]) => {
      const box = strip(heading, entries, empty);
      box.querySelector('.wchips')?.append(...entries.slice(0, 8).map(whenChip));
      return box;
    });
    byId('cal-summary').replaceChildren(...summary);
    // Twelve months from this one; each festival sits in the month its next (or current) run starts.
    const first = new Date(today.getFullYear(), today.getMonth(), 1);
    const months = Array.from({ length: 12 }, (_, index) => new Date(first.getFullYear(), first.getMonth() + index, 1));
    const key = date => date.getFullYear() * 12 + date.getMonth();
    const byMonth = new Map(months.map(date => [key(date), []]));
    for (const entry of calendarEntries()) byMonth.get(key(entry.when.start))?.push(entry);
    byId('cal-months').replaceChildren(...months.map(date => {
      const entries = byMonth.get(key(date)).sort((a, b) => Boolean(b.guide) - Boolean(a.guide) || a.when.start - b.when.start);
      const box = panel(`${MONTHS[date.getMonth()]} ${date.getFullYear()} · ${number(entries.length)}`);
      if (key(date) === key(today)) box.classList.add('current');
      const rows = entries.slice(0, 12).map(entry => {
        const row = button('', 'crow', () => openEntry(entry));
        row.append(element('b', entry.record.short || entry.record.name), element('span', entry.when.status === 'month' ? 'likely on now' : entry.when.sure && entry.when.status !== 'over' ? entry.when.brief : 'dates TBC', `when ${entry.when.status}`));
        row.title = `${entry.record.name} · ${entry.when.text}`;
        return row;
      });
      box.append(...(rows.length ? rows : [element('p', 'No festivals on record.', 'meta')]));
      if (entries.length > 12) box.append(element('p', `and ${number(entries.length - 12)} more`, 'meta'));
      return box;
    }));
  }
  const previous = byId('previous');
  const next = byId('next');
  let items = [];
  let page = 0;
  let pageCount = 1;

  // Festival chips, like the LitFest Guide strip.
  const chips = ['', ...festivalMap.keys()].map(id => {
    const record = festivalMap.get(id);
    const chip = button(record?.short || 'All', 'fchip', () => go(id, id ? 'discover' : 'home'));
    if (record?.logo) {
      const img = element('img');
      img.src = record.logo.file;
      img.alt = '';
      chip.prepend(img);
      chip.title = record.name;
    }
    return chip;
  });
  byId('festival-strip').append(...chips);

  // Detail sheet
  function open(title, category) {
    const heading = element('h2', title);
    heading.id = 'detail-title';
    content.replaceChildren(element('p', category, 'tag'), heading);
    if (!detail.open) detail.showModal();
    detail.scrollTop = 0;
  }
  function list(heading, values) {
    if (!values.length) return;
    const ul = element('ul');
    for (const value of values) {
      const li = element('li');
      li.append(value);
      ul.append(li);
    }
    content.append(element('h3', heading), ul);
  }
  function showFilm(film) {
    const record = festivalMap.get(film.festival);
    const event = record.editions.find(entry => entry.year === film.year);
    open(film.title, [label(film), film.format !== UNLISTED && film.format].filter(Boolean).join(' · '));
    if (film.artwork) {
      const figure = element('figure', '', 'film-artwork');
      const caption = element('figcaption');
      caption.append(source(film.artwork.source, film.artwork.credit));
      figure.append(thumbnail('', film.artwork), caption);
      content.append(figure);
    }
    const facts = [film.language, film.country, film.section, film.minutes && `${film.minutes} min`, film.genres?.join(', ')].filter(Boolean).join(' · ');
    if (facts) content.append(element('p', facts, 'meta'));
    if (film.summary) content.append(element('p', film.summary));
    if (film.cataloguePage) content.append(element('p', `Catalogue index · printed page ${film.cataloguePage}`, 'meta'));
    // Videos recorded on Wikidata; YouTube decides what plays in each country.
    list('Watch on YouTube', (film.youtube || []).map(([id, kind], index) => source(`https://www.youtube.com/watch?v=${id}`, `${kind === 'trailer' ? 'Trailer' : 'Video'}${film.youtube.length > 1 ? ` ${index + 1}` : ''} on YouTube`)));
    list('Credits', film.credits.map(([role, name]) => {
      const row = element('span', `${role} · `);
      row.append(button(name, 'credit-link', () => showPerson(name)));
      return row;
    }));
    list('Awards', film.awards.map(award => source(award[1], [award[0], award[2]].filter(Boolean).join(' · '))));
    const references = film.sources.filter(url => url !== event.source);
    if (film.checked) content.append(element('p', `Award details ${film.checked} from the sources below.`, 'meta'));
    list('Sources', [source(event.source, editionLabel(event)), source(record.url, 'Official festival website'), ...references.map((url, index) => source(url, film.fromCatalogue ? 'Film catalogue' : `Film reference ${index + 1}`)), film.wikidata && source(`https://www.wikidata.org/wiki/${film.wikidata}`, 'Wikidata'), film.imdb && source(`https://www.imdb.com/title/${film.imdb}/`, 'IMDb')].filter(Boolean));
  }
  function showPerson(name) {
    open(name, 'Person');
    const portrait = portraits[name];
    if (portrait) {
      const figure = element('figure', '', 'profile-photo');
      const caption = element('figcaption');
      caption.append(source(portrait.source, portrait.credit));
      if (portrait.license) caption.append(' · ', source(portrait.license, portrait.licenseName));
      figure.append(thumbnail('', portrait), caption);
      content.append(figure);
    }
    list('Festival credits and honours', people.get(name).map(record => {
      const row = element('span', `${record.role} · `);
      row.append(record.film ? button(record.film.title, 'credit-link', () => showFilm(record.film)) : source(record.award[1], record.award[0]), ` · ${label(record)}`);
      return row;
    }));
  }
  function showAward(record) {
    const [name, url, recipient] = record.award;
    open(name, label(record));
    if (recipient) content.append(people.has(recipient) ? button(recipient, 'credit-link', () => showPerson(recipient)) : element('p', recipient));
    if (record.film) list('Film', [button(record.film.title, 'credit-link', () => showFilm(record.film))]);
    list('Source', [source(url, 'Award announcement')]);
  }
  function showEdition(record, event) {
    open(`${record.short} ${event.year}`, editionLabel(event));
    const count = filmsIn(record.id, event.year).length;
    content.append(element('p', count ? `${number(count)} films on record from this edition.` : 'The catalogue is available as a PDF. Indexed titles are still to come.', 'meta'));
    list('Documents', [
      event.catalogue && source(event.catalogue, event.catalogueLabel || 'Edition catalogue PDF'),
      event.source && event.source !== event.catalogue && source(event.source, 'Edition source'),
      ...(event.archiveDocuments || []).map(doc => source(doc.url, doc.name))
    ].filter(Boolean));
    if (count) content.append(button('Browse these films', 'btn', () => {
      detail.close();
      edition.value = String(event.year);
      go(record.id, 'films', false);
    }));
  }
  function showAbout() {
    open('About FilmFest Guide', 'About');
    const G = 'https://github.com/omshivaprakash/filmfest-guide';
    const about = element('div', '', 'about');
    // Each part is text or a [url, label] link, so the copy reads as plain sentences.
    const section = (heading, ...parts) => {
      const p = element('p');
      for (const part of parts) p.append(Array.isArray(part) ? source(...part) : part);
      about.append(...(heading ? [element('h3', heading)] : []), p);
    };
    section('', `An independent, non-commercial guide to what screens at film festivals, starting with India: ${number(films.length)} films, ${number(people.size)} people and ${number(festivals.reduce((sum, record) => sum + record.editions.length, 0))} editions from ${festivals.length} festivals so far, plus ${number(worldFestivals.length)} festivals around the world listed and waiting to be added. It is built for education and research, and is not affiliated with, endorsed by or sponsored by any festival.`);
    section('', 'It is the companion to ', ['https://omshivaprakash.github.io/litfest-speaker-guide/', 'LitFest Guide'], ', the guide to literature festivals, and is built the same way.');
    section('Where the information comes from', 'Film records come from each festival’s official catalogues, schedules and award announcements, the Press Information Bureau for Goa’s Indian Panorama, and the Servants of Knowledge collection on the Internet Archive for older Bengaluru catalogues. The world festival list comes from ', ['https://www.wikidata.org/', 'Wikidata'], ', with short descriptions from English Wikipedia and logos from Wikimedia Commons. Trailers and full films on YouTube are the ones Wikidata records for a film. Every record links to its source, and the festival’s own site is always the final word.');
    section('What to keep in mind', 'Older catalogues are scans, so some editions have gaps or no indexed titles yet; a PDF link means the source exists even when its titles are still to come. The People directory is built from the credits, so a spelling variant counts as a separate person. Film countries are tidied to one spelling per country so the map can count them. Maps place a country or city by one point and are schematic.');
    section('How festival types are worked out', 'Each world festival can carry types such as documentary, short film, animation, LGBTQ+, children and youth, or horror, fantasy and sci-fi. They come from the festival’s classes and genres on Wikidata plus words in its name and description, so treat them as a guide. A festival can have more than one type, and many have none.');
    section('Open data', 'The facts here (which films screened where and when, their credits and awards, festival dates, and the tables built from them) are open data under ', ['https://creativecommons.org/licenses/by/4.0/', 'CC BY 4.0'], ': free to use with attribution. The Wikidata list is CC0 and Wikipedia descriptions are CC BY-SA 4.0. See ', [`${G}/blob/main/LICENSE-DATA.md`, 'the data licence'], ' and ', [`${G}/blob/main/CITATION.cff`, 'how to cite'], '. The code is MIT.');
    section('Stills, posters, portraits and logos', 'These belong to their owners and are shown only to identify a film, person or festival. Images from Wikimedia Commons keep their own licence and are credited where they appear. Nothing here is for sale.');
    section('Your privacy', 'No account, no tracking, no analytics and no cookies. Pages, data, fonts and images are served from this site, so opening it sends nothing to anyone else. Links to festival sites and YouTube open only when you tap them.');
    section('Language (beta)', 'Menus, headings and buttons can be shown in Kannada or Hindi. Film titles, names, descriptions and festival data stay as published. These translations are new, so corrections from native speakers are welcome on GitHub.');
    about.append(document.querySelector('#home .lsw').cloneNode(true));
    section('Use it as an app', 'The site is plain files with no server of its own. Add it to your home screen from your browser’s menu, and it opens offline once you have visited.');
    section('Corrections, removal and contact', 'Spotted a mistake, or want a film, name, image or festival changed or removed? ', [`${G}/issues/new`, 'Open an issue on GitHub'], ' and say what and where. Festivals and the people listed here are welcome to ask.');
    section('', 'Code, data and documentation: ', [G, 'github.com/omshivaprakash/filmfest-guide'], ' · Built by ', ['https://omshivaprakash.github.io/', 'omshivaprakash'], '.');
    content.append(about);
  }
  byId('open-about').addEventListener('click', showAbout);
  byId('open-explore').addEventListener('click', () => go('', 'map'));
  for (const link of document.querySelectorAll('[data-go]')) link.addEventListener('click', () => go('', link.dataset.go));
  byId('open-search').addEventListener('click', () => {
    go('', 'films');
    search.focus();
  });

  // Cards
  function result(tag, title, subtitle, action, icon = '', photo) {
    return () => {
      const card = button('', 'result', action);
      const copy = element('span', '', 'result-copy');
      copy.append(element('span', tag, 'tag'), element('span', title, 'card-title'), element('span', subtitle, 'card-copy'));
      card.append(thumbnail(icon, photo), copy);
      return card;
    };
  }
  function kpis(target, values) {
    target.replaceChildren(...values.map(([value, caption]) => {
      const tile = element('div', '', 'kpi');
      tile.append(element('b', typeof value === 'number' ? number(value) : value), element('span', caption));
      return tile;
    }));
  }
  const filmLine = film => [film.format !== UNLISTED && film.format, film.language, film.country].filter(Boolean).join(' · ');

  // Home
  function renderHome() {
    const years = festivals.flatMap(record => record.editions.map(event => event.year));
    const countries = unique([...festivals, ...worldFestivals].map(record => record.country).filter(Boolean));
    kpis(byId('home-kpis'), [
      [festivals.length + worldFestivals.length, 'film festivals worldwide'],
      [countries.length, 'countries with a festival'],
      [films.length, `films on record from the ${festivals.length} festivals in the guide`],
      [people.size, 'people credited'],
      [years.length, `festival editions, ${Math.min(...years)} to ${Math.max(...years)}`],
      [awards.length, 'awards and honours']
    ]);
    byId('festival-cards').replaceChildren(...festivals.map(record => {
      const latest = record.editions[0];
      const card = button('', 'fcard', () => go(record.id, 'discover'));
      const img = element('img');
      if (record.logo) img.src = record.logo.file;
      img.alt = '';
      const copy = element('span');
      copy.append(element('h3', record.name), element('span', editionLabel(latest), 'd'), element('span', record.region, 'r'));
      const count = record.editions.length;
      const when = whenOf(record);
      if (when) copy.append(whenBadge(when));
      card.append(record.logo ? img : element('span', initials(record.short), 'thumbnail'), copy, element('span', `${count} edition${count === 1 ? '' : 's'}`, 'badge'));
      return card;
    }), (() => {
      const card = button('', 'fcard wipcard', () => go('', 'world'));
      const copy = element('span');
      copy.append(element('h3', `${number(worldFestivals.length)} more festivals worldwide`), element('span', 'Cannes, Berlinale, Busan, MAMI, FESPACO and more, with logos and descriptions. Films and people to come.', 'd'), element('span', 'Work in progress', 'r'));
      card.append(element('span', '🌍', 'thumbnail'), copy, element('span', `${regions.length} regions`, 'badge wip'));
      return card;
    })());
    byId('home-when').replaceChildren(...[['Happening now', onNow()], ['Next up', comingNext()]].filter(([, entries]) => entries.length).map(([heading, entries]) => {
      const box = panel(heading, element('div', '', 'wchips'));
      box.lastChild.append(...entries.slice(0, 6).map(whenChip), button('Full calendar ›', 'hlink', () => go('', 'calendar')));
      return box;
    }));
    const homeMap = byId('home-map');
    homeMap.replaceChildren(worldMap(festivalPoints()));
    const winners = films.filter(film => film.awards.length && film.artwork).slice(0, 6);
    byId('home-shelf').replaceChildren(...winners.map(filmCard));
    renderHomeStats();
    renderSync();
  }
  // Open the World festivals list with one filter set.
  function worldWith(control, value) {
    go('', 'world');
    control.value = value;
    renderList();
  }
  const panel = (heading, ...children) => {
    const box = element('div', '', 'panel');
    box.append(element('h5', heading), ...children);
    return box;
  };
  function renderHomeStats() {
    const stats = [];
    // Festival of the month: the best-known hand-listed festival usually held this month (worldFestivals is sorted by Wikipedia links).
    const month = new Date().toLocaleString('en-GB', { month: 'long' });
    const thisMonth = worldFestivals.filter(record => record.month?.includes(month));
    if (thisMonth.length) {
      const [pick, ...others] = thisMonth;
      const card = button('', 'fom', () => showWorld(pick));
      const copy = element('span');
      copy.append(element('b', pick.name), element('span', [[pick.city, pick.country].filter(Boolean).join(', '), `usually ${pick.month}`].join(' · '), 'd'), element('span', pick.desc ? pick.desc.charAt(0).toUpperCase() + pick.desc.slice(1) : '', 'd'));
      card.append(thumbnail(initials(pick.short || pick.name), pick.logo), copy);
      const also = element('p', others.length ? 'Also this month: ' : '', 'meta');
      others.slice(0, 4).forEach((record, index) => also.append(index ? ', ' : '', button(record.short || record.name, 'credit-link', () => showWorld(record))));
      stats.push(panel(`Festival of the month · ${month}`, card, also));
    }
    const types = tally(worldFestivals, record => record.types || []);
    if (types.length) stats.push(panel(`Festivals by type · ${types.length} types`, ...barList(types.slice(0, 8).map(([name, count]) => [name, count, () => worldWith(kind, name)]))));
    const decades = new Map();
    for (const record of worldFestivals) if (record.since) {
      const decade = Math.max(1940, Math.floor(record.since / 10) * 10);
      decades.set(decade, (decades.get(decade) || 0) + 1);
    }
    if (decades.size > 1) {
      const peak = Math.max(...decades.values());
      const bars = element('div', '', 'bars');
      for (let decade = 1940; decade <= Math.max(...decades.keys()); decade += 10) {
        const count = decades.get(decade) || 0;
        const bar = element('div');
        bar.title = `${decade === 1940 ? '1940s and earlier' : `${decade}s`}: ${number(count)} festivals founded`;
        const fill = element('i');
        fill.style.height = `${Math.round((count / peak) * 100)}%`;
        bar.append(fill, element('small', `'${String(decade).slice(2)}s`));
        bars.append(bar);
      }
      stats.push(panel('Founded by decade', bars, element('p', `${number([...decades.values()].reduce((a, b) => a + b, 0))} festivals with a known founding year`, 'meta')));
    }
    const byCountry = tally(worldFestivals, record => [record.country]);
    if (byCountry.length) stats.push(panel(`Top countries · ${byCountry.length} in all`, ...barList(byCountry.slice(0, 8).map(([name, count]) => [name, count, () => worldWith(search, name)]))));
    byId('home-stats').replaceChildren(...stats);
    const notable = worldFestivals.filter(record => record.logo).slice(0, 12);
    byId('home-logos').previousElementSibling.hidden = !notable.length;
    byId('home-logos').replaceChildren(...notable.map(record => {
      const tile = button('', 'logo', () => showWorld(record));
      tile.title = `${record.name} · ${record.city || record.country}`;
      tile.append(thumbnail(initials(record.short || record.name), record.logo, 'lg'), element('span', record.short || record.name));
      return tile;
    }));
  }
  // Data freshness: sync.json lists each source; a scheduled extractor stamps data/<id>/sync.json only when its data changes.
  let syncSources;
  function renderSync() {
    syncSources ||= fetch('sync.json').then(reply => (reply.ok ? reply.json() : { sources: [] })).then(({ sources }) => Promise.all(sources.map(entry => (entry.updated
      ? entry
      : fetch(`data/${entry.id}/sync.json`).then(reply => (reply.ok ? reply.json() : {})).catch(() => ({})).then(stamp => ({ ...entry, ...stamp })))))).catch(() => []);
    syncSources.then(sources => {
      const rows = sources.map(entry => {
        const days = entry.updated ? Math.round((Date.now() - new Date(entry.updated)) / 864e5) : null;
        const when = days === null ? 'not synced yet' : `updated ${new Intl.RelativeTimeFormat('en', { numeric: 'auto' }).format(-days, 'day')}`;
        const row = element('li');
        row.append(element('b', entry.label), ` · ${when}`, entry.records ? ` · ${number(entry.records)} records` : '', entry.schedule ? ` · refreshed ${entry.schedule}` : '');
        return row;
      });
      byId('sync-list').replaceChildren(...rows);
      byId('home-sync').hidden = !rows.length;
    });
  }

  // Discover
  function renderDiscover(record) {
    const latest = record.editions[0];
    const recent = filmsIn(record.id, latest.year);
    const all = filmsIn(record.id);
    const credited = unique(all.flatMap(film => film.credits.map(([, name]) => name)));
    const recordAwards = awards.filter(entry => entry.festival === record.id);
    byId('d-kicker').textContent = [latest.dates && `${latest.dates} ${latest.year}`, record.region].filter(Boolean).join(' · ');
    byId('d-title').textContent = `${record.name} ${latest.year}`;
    byId('d-sub').textContent = record.description;
    kpis(byId('d-kpis'), [
      [recent.length, `films from the ${latest.number || latest.year} edition`],
      [all.length, 'films across all editions'],
      [credited.length, 'people credited'],
      [recordAwards.length, 'awards and honours']
    ]);
    const counts = [...record.editions].reverse().map(event => [event.year, filmsIn(record.id, event.year).length]);
    const peak = Math.max(1, ...counts.map(([, count]) => count));
    byId('d-bars').replaceChildren(...counts.map(([year, count]) => {
      const bar = element('div');
      bar.title = `${year}: ${count} films`;
      const fill = element('i');
      fill.style.height = `${Math.round((count / peak) * 100)}%`;
      bar.append(fill, element('small', `'${String(year).slice(2)}`));
      return bar;
    }));
    byId('discover').querySelector('.panel').hidden = counts.length < 2;
    // Award winners first, then films with artwork from the latest edition.
    const picks = unique([
      ...all.filter(film => film.awards.length && film.artwork),
      ...recent.filter(film => film.artwork),
      ...all.filter(film => film.artwork),
      ...all
    ]).slice(0, 18);
    byId('d-shelf-title').textContent = picks.some(film => film.awards.length) ? 'Start here: award winners and new films' : 'Start here';
    byId('d-shelf').replaceChildren(...picks.map(filmCard));
    fitShelf();
  }
  function filmCard(film) {
    const card = button('', 'card', () => showFilm(film));
    card.append(thumbnail('▶', film.artwork, 'ph'), element('span', film.title, 'nm'), element('span', film.awards[0]?.[0] || filmLine(film) || label(film), 'ln'));
    return card;
  }
  // One screen per view: drop shelf cards that would be cut off at the bottom.
  function fitShelf() {
    const shelf = byId('d-shelf');
    for (const card of [...shelf.children]) card.hidden = false;
    for (const card of [...shelf.children]) card.hidden = card.offsetTop + card.offsetHeight > shelf.clientHeight;
  }

  let aboutTexts;
  const worldAbout = () => (aboutTexts ||= Promise.all([optional('data/world-festivals/world-about.json'), optional('data/enrich/about.json')]).then(([english, other]) => ({ ...other?.festivals, ...english })));
  function showWorld(record) {
    open(record.name, `${record.region} · Work in progress`);
    if (record.logo) {
      const img = element('img', '', 'wlogo');
      img.src = record.logo.file;
      img.alt = `${record.name} logo`;
      content.append(img);
    }
    const place = [record.city, record.country].filter(Boolean).join(', ');
    const facts = [place + (record.approx ? ' (map position approximate)' : ''), record.since && `since ${record.since}`, record.every, record.month && `usually ${record.month}`, record.langs && `in ${record.langs.join(', ')}`].filter(Boolean).join(' · ');
    if (record.fiapf) content.append(element('p', record.fiapf === 'A-list' ? 'FIAPF A-list festival' : 'FIAPF accredited', 'tag'));
    if (record.types) content.append(element('p', `Type: ${record.types.join(', ')}`, 'meta'));
    content.append(element('p', facts, 'meta'));
    const when = whenOf(record);
    if (when) content.append(whenBadge(when));
    const about = element('p', record.desc ? record.desc.charAt(0).toUpperCase() + record.desc.slice(1) + '.' : '');
    content.append(about);
    worldAbout().then(texts => {
      const text = texts[record.id];
      if (!text) return;
      about.textContent = text.text || text;
      if (text.lang) about.lang = text.lang;
    });
    content.append(element('p', 'Listed so we can plan its import. Films, people and past editions will be added from its official catalogues.', 'meta'));
    list('Sources', [
      record.url && source(record.url, 'Official festival website'),
      record.wiki && source(record.wiki, /^https:\/\/en\./.test(record.wiki) ? 'Wikipedia' : `Wikipedia (${record.wiki.split('//')[1].split('.')[0]})`),
      /^Q\d+$/.test(record.id) && source(`https://www.wikidata.org/wiki/${record.id}`, 'Wikidata')
    ].filter(Boolean));
    if (record.logo) {
      const credit = element('p', `Logo: ${record.logo.credit || 'Wikimedia Commons'}, `, 'meta');
      credit.append(source(record.logo.licenseUrl || record.logo.source, record.logo.license || 'see licence'), ' via ', source(record.logo.source, 'Wikimedia Commons'));
      content.append(credit);
    }
  }
  function showCountry(country, scoped) {
    const list_ = scoped.filter(film => countriesOf(film).includes(country));
    const credited = unique(list_.flatMap(film => film.credits.map(([, name]) => name)));
    open(country, `${number(list_.length)} films · ${number(credited.length)} people credited`);
    list('Films', list_.slice(0, 12).map(film => {
      const row = element('span');
      row.append(button(film.title, 'credit-link', () => showFilm(film)), ` · ${label(film)}`);
      return row;
    }));
    content.append(button(`Search all films mentioning ${country}`, 'btn', () => {
      detail.close();
      search.value = country;
      edition.value = '';
      facet.value = '';
      go(festivalId, 'films', false);
    }));
  }

  // Explore: maps and bar lists
  let mapMode = 'films';
  function svgNode(tag, attrs) {
    const node = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (const [key, value] of Object.entries(attrs)) node.setAttribute(key, value);
    return node;
  }
  function worldMap(points) {
    const [W, H, x0, x1, y0, y1] = [720, 330, -180, 180, -56, 80];
    const px = lon => ((lon - x0) / (x1 - x0)) * W;
    const py = lat => ((y1 - lat) / (y1 - y0)) * H;
    const svg = svgNode('svg', { class: 'map', viewBox: `0 0 ${W} ${H}`, role: 'img', 'aria-label': 'World map' });
    for (let lon = -150; lon <= 180; lon += 30) svg.append(svgNode('path', { class: 'grat', d: `M${px(lon)} 0V${H}` }));
    for (let lat = -30; lat <= 60; lat += 30) svg.append(svgNode('path', { class: 'grat', d: `M0 ${py(lat)}H${W}` }));
    for (const outline of Object.values(LAND)) svg.append(svgNode('polygon', { class: 'land', points: outline.map(([lon, lat]) => `${px(lon).toFixed(1)},${py(lat).toFixed(1)}`).join(' ') }));
    const peak = Math.max(1, ...points.map(point => point.count || 1));
    for (const point of [...points].sort((a, b) => (b.count || 1) - (a.count || 1))) {
      const r = point.r || 2.5 + Math.sqrt((point.count || 1) / peak) * 16;
      const dot = svgNode('circle', { cx: px(point.lon).toFixed(1), cy: py(point.lat).toFixed(1), r: r.toFixed(1), tabindex: 0, class: point.className || '' });
      const title = svgNode('title', {});
      title.textContent = point.title;
      dot.append(title);
      dot.addEventListener('click', point.action);
      dot.addEventListener('keydown', event => { if (event.key === 'Enter') point.action(); });
      svg.append(dot);
    }
    return svg;
  }
  function barList(rows) {
    const peak = Math.max(1, ...rows.map(([, count]) => count));
    return rows.map(([name, count, action]) => {
      const row = button('', 'vb', action);
      const fill = element('i');
      fill.style.width = `${Math.max(1, (count / peak) * 100)}%`;
      row.append(element('span', name), fill, element('em', number(count)));
      row.title = `${name}: ${number(count)}`;
      return row;
    });
  }
  const tally = (records, keysOf) => {
    const counts = new Map();
    for (const record of records) for (const key of keysOf(record)) counts.set(key, (counts.get(key) || 0) + 1);
    return [...counts].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
  };
  function festivalPoints() {
    return [
      ...worldFestivals.map(record => ({ lon: record.lon, lat: record.lat, r: record.links > 30 ? 3.5 : 2, className: 'wip', title: `${record.name} · ${record.city || record.country} · work in progress`, action: () => showWorld(record) })),
      ...festivals.map(record => ({ lon: record.lon, lat: record.lat, r: 6, title: `${record.name} · in the guide`, action: () => go(record.id, 'discover') }))
    ];
  }
  function renderExplore() {
    const scoped = festivalId ? filmsIn(festivalId) : films;
    const scopeName = festivalMap.get(festivalId)?.short || 'all festivals';
    const grid = byId('explore').querySelector('.exgrid');
    const modes = view === 'map' ? { films: 'Films', people: 'People', ...(festivalId ? {} : { festivals: 'Festivals' }) }
      : view === 'roles' ? Object.fromEntries(ROLES.map(role => [role, role]))
      : view === 'impact' ? { later: 'What winners won next', festivals: 'By festival', returns: 'Did winning directors return?' } : {};
    if (!modes[mapMode]) mapMode = Object.keys(modes)[0] || 'films';
    byId('ex-mode').replaceChildren(...Object.entries(modes).map(([key, text]) => {
      const pill = button(text, 'pill', () => { mapMode = key; renderExplore(); });
      pill.setAttribute('aria-pressed', String(key === mapMode));
      return pill;
    }));
    const mapBox = byId('ex-map');
    const bars = byId('ex-bars');
    grid.classList.toggle('wide', ['languages', 'roles', 'impact'].includes(view));
    if (view === 'roles') return renderRoles(scoped, scopeName, bars);
    if (view === 'impact') return renderImpact(scoped, scopeName, bars);
    if (view === 'languages') {
      const rows = tally(scoped, languagesOf);
      byId('ex-note').textContent = `${rows.length} languages named across ${number(scoped.filter(film => film.language).length)} of ${number(scoped.length)} films in ${scopeName}. Tap a language to see its films.`;
      bars.replaceChildren(...barList(rows.map(([name, count]) => [name, count, () => {
        search.value = name;
        edition.value = '';
        facet.value = '';
        go(festivalId, 'films', false);
      }])));
      return;
    }
    if (mapMode === 'festivals') {
      const all = festivalPoints();
      byId('ex-note').textContent = `${festivals.length} festivals in the guide and ${number(worldFestivals.length)} listed as work in progress. Tap a dot for details.`;
      mapBox.replaceChildren(worldMap(all));
      const legend = element('div', '', 'legend');
      legend.innerHTML = '<span><i></i>In the guide</span><span><i class="wip"></i>Work in progress</span>';
      bars.replaceChildren(legend, ...barList(tally(worldFestivals, record => [record.region]).map(([region, count]) => [region, count, () => {
        search.value = '';
        go('', 'world', false);
        facet.value = region;  // the region options exist only once the world list has rendered
        renderList();
      }])), element('h5', 'Countries with the most festivals'), ...barList(tally(worldFestivals, record => [record.country]).slice(0, 15).map(([country, count]) => [country, count, () => {
        search.value = country;
        go('', 'world', false);
      }])), element('h5', 'Festival types'), ...barList(tally(worldFestivals, record => record.types || []).map(([name, count]) => [name, count, () => {
        search.value = '';
        go('', 'world', false);
        kind.value = name;  // the type options exist only once the world list has rendered
        renderList();
      }])), element('h5', 'Founded, by decade'), ...barList(tally(worldFestivals.filter(record => record.since > 1800 && record.since <= new Date().getFullYear()), record => [`${Math.floor(record.since / 10) * 10}s`]).sort((a, b) => a[0].localeCompare(b[0])).map(([decade, count]) => [decade, count, () => {
        const start = Number.parseInt(decade, 10);
        open(`Festivals founded in the ${decade}`, `${number(count)} festivals`);
        list('Oldest first', worldFestivals.filter(record => record.since >= start && record.since < start + 10).sort((a, b) => a.since - b.since || (b.links || 0) - (a.links || 0)).slice(0, 40).map(record => {
          const row = element('span');
          row.append(button(record.name, 'credit-link', () => showWorld(record)), ` · ${record.since} · ${record.country}`);
          return row;
        }));
      }])));
      return;
    }
    let rows;
    if (mapMode === 'people') {
      // A person's countries are the production countries of the films they are credited on.
      const perPerson = new Map();
      for (const film of scoped) for (const [, name] of film.credits) {
        if (!perPerson.has(name)) perPerson.set(name, new Set());
        for (const country of countriesOf(film)) perPerson.get(name).add(country);
      }
      rows = tally([...perPerson.values()], set => set);
      const located = [...perPerson.values()].filter(set => set.size).length;
      byId('ex-note').textContent = `${number(located)} of ${number(perPerson.size)} credited people in ${scopeName}, placed by the production countries of their films.`;
    } else {
      rows = tally(scoped, countriesOf);
      byId('ex-note').textContent = `${number(scoped.filter(film => film.country).length)} of ${number(scoped.length)} films in ${scopeName} name a production country. Co-productions count once for each country.`;
    }
    const noun = mapMode === 'people' ? 'people' : 'films';
    mapBox.replaceChildren(worldMap(rows.filter(([country]) => POS[country]).map(([country, count]) => ({ lon: POS[country][0], lat: POS[country][1], count, title: `${country}: ${number(count)} ${noun}`, action: () => showCountry(country, scoped) }))));
    bars.replaceChildren(...barList(rows.map(([country, count]) => [country, count, () => showCountry(country, scoped)])));
  }

  function filmDialog(title, category, list_) {
    open(title, category);
    list('Films', list_.map(film => {
      const row = element('span');
      row.append(button(film.title, 'credit-link', () => showFilm(film)), ` · ${label(film)}`);
      return row;
    }));
  }
  // Roles: people per craft, ranked by the festival awards on record for the films they made in that role.
  function renderRoles(scoped, scopeName, bars) {
    const byPerson = new Map();
    const entry = name => byPerson.get(name) || byPerson.set(name, { films: [], awards: 0, fests: new Set() }).get(name);
    for (const film of scoped) for (const [role, name] of film.credits) {
      if (role !== mapMode || entry(name).films.includes(film)) continue;
      Object.assign(entry(name), { awards: entry(name).awards + film.awards.length }).films.push(film);
      entry(name).fests.add(film.festival);
    }
    for (const honor of honors) if (honor.role === mapMode && honor.award[2] && (!festivalId || honor.festival === festivalId)) {
      entry(honor.award[2]).awards += 1;
      entry(honor.award[2]).fests.add(honor.festival);
    }
    const rows = [...byPerson];
    const films_ = unique(rows.flatMap(([, e]) => e.films)).length;
    byId('ex-note').textContent = `${number(rows.length)} people credited as ${mapMode.toLowerCase()} on ${number(films_)} films in ${scopeName}. “Most awarded” counts the festival awards on record in this guide for their festival selections in this role (plus honours given to them as ${mapMode.toLowerCase()}); it is a measure of festival recognition here, not a judgement of who is best. Tap a name for their credits.`;
    const films = count => `${count} selection${count === 1 ? '' : 's'}`;
    const awarded = rows.filter(([, e]) => e.awards).sort(([an, a], [bn, b]) => b.awards - a.awards || b.fests.size - a.fests.size || an.localeCompare(bn)).slice(0, 40);
    const travelled = rows.filter(([, e]) => e.fests.size > 1).sort(([an, a], [bn, b]) => b.fests.size - a.fests.size || b.films.length - a.films.length || an.localeCompare(bn)).slice(0, 20);
    bars.replaceChildren(
      element('h5', 'Most awarded'), ...(awarded.length ? barList(awarded.map(([name, e]) => [`${name} · ${films(e.films.length)}`, e.awards, () => showPerson(name)])) : [element('p', 'No awards on record for this role here yet.', 'meta')]),
      element('h5', 'Shown at the most festivals'), ...(travelled.length ? barList(travelled.map(([name, e]) => [`${name} · ${films(e.films.length)}`, e.fests.size, () => showPerson(name)])) : [element('p', 'Nobody in this role has films at more than one festival here yet.', 'meta')]));
  }
  // Award impact: what festival winners went on to win (Wikidata, via the award-impact extractor), and whether winning directors came back.
  let impactData;
  let impactLoad;
  const MAJOR = [['Academy Awards', /^Academy Award/], ['BAFTA Awards', /BAFTA|British Academy/], ['Golden Globes', /^Golden Globe/], ['European Film Awards', /^European Film Award/], ['César Awards', /^César/], ['Goya Awards', /^Goya Award/], ['Independent Spirit Awards', /^Independent Spirit/], ['National Film Awards (India)', /^National Film Award/]];
  function laterAwards(film) {
    const record = impactData[film.wikidata];
    if (!record) return null;
    const event = festivalMap.get(film.festival);
    const own = new Set(film.awards.flatMap(([name, url]) => [normalize(name), String(url).match(/Q\d+$/)?.[0]]));
    const elsewhere = ([name, qid, year]) => year && year >= film.year && !own.has(qid) && !own.has(normalize(name)) && ![event.short, event.name].some(text => text && name.includes(text));
    return { won: record.won.filter(elsewhere), nominated: record.nominated.filter(elsewhere) };
  }
  function renderImpact(scoped, scopeName, bars) {
    const note = byId('ex-note');
    if (!impactData) {
      note.textContent = 'Loading award records…';
      bars.replaceChildren();
      impactLoad ||= optional('data/award-impact/impact.json').then(data => {
        impactData = data?.films || {};
        if (view === 'impact') renderExplore();
      });
      return;
    }
    const winners = scoped.filter(film => film.awards.length);
    if (mapMode === 'returns') {
      // From the guide alone: a winning director "returned" when a later edition of any festival here shows another film of theirs.
      const directed = new Map();
      for (const film of films) for (const [role, name] of film.credits) if (role === 'Director') (directed.get(name) || directed.set(name, []).get(name)).push(film);
      const back = new Map();
      for (const film of winners) for (const [role, name] of film.credits) if (role === 'Director') {
        const next = directed.get(name).filter(other => other.year > film.year && other.title !== film.title);
        const was = back.get(name);
        if (!was || next.length > was.next.length) back.set(name, { film, next });
      }
      const all = [...back];
      const returned = all.filter(([, e]) => e.next.length);
      note.textContent = `${number(returned.length)} of ${number(all.length)} directors of award-winning films in ${scopeName} came back with another film at a later edition of a festival in this guide. Counted from the guide’s own records only, so recent winners have had less time to return.`;
      const perFestival = tally(returned.map(([, e]) => e.film), film => [film.festival]);
      const total = new Map(tally(all.map(([, e]) => e.film), film => [film.festival]));
      bars.replaceChildren(element('h5', 'Returning winners, by festival where they first won'), ...barList(perFestival.map(([id, count]) => [`${festivalMap.get(id).short} · of ${number(total.get(id))} winning directors`, count, () => filmDialog(`${festivalMap.get(id).short}: winners who came back`, 'Their winning films', returned.filter(([, e]) => e.film.festival === id).map(([, e]) => e.film))])),
        element('h5', 'Came back most often'), ...barList(returned.sort(([an, a], [bn, b]) => b.next.length - a.next.length || an.localeCompare(bn)).slice(0, 25).map(([name, e]) => [name, e.next.length, () => showPerson(name)])));
      return;
    }
    const checked = winners.filter(film => film.wikidata && impactData[film.wikidata]).map(film => ({ film, later: laterAwards(film) }));
    const wonMore = checked.filter(entry => entry.later.won.length);
    note.textContent = `${number(checked.length)} of ${number(winners.length)} award-winning films in ${scopeName} have award records on Wikidata; ${number(wonMore.length)} of those won something else in the same year or later. The other ${number(winners.length - checked.length)} are not checked: they have no Wikidata link yet, so nothing is claimed about them. Awards without a recorded year are left out.`;
    if (mapMode === 'festivals') {
      const perFestival = tally(wonMore.map(entry => entry.film), film => [film.festival]);
      const total = new Map(tally(checked.map(entry => entry.film), film => [film.festival]));
      bars.replaceChildren(element('h5', 'Winners that went on to win elsewhere'), ...barList(perFestival.map(([id, count]) => [`${festivalMap.get(id).short} · of ${number(total.get(id))} checked winners`, count, () => filmDialog(`${festivalMap.get(id).short}: winners that won elsewhere`, 'Wikidata award records', wonMore.filter(entry => entry.film.festival === id).map(entry => entry.film))])));
      return;
    }
    const major = MAJOR.flatMap(([group, pattern]) => ['won', 'nominated'].map(kind => {
      const hits = checked.filter(entry => entry.later[kind].some(([name]) => pattern.test(name))).map(entry => entry.film);
      return [`${group} · ${kind}`, hits.length, () => filmDialog(`Festival winners ${kind === 'won' ? 'that won' : 'nominated for'} ${group}`, 'Wikidata award records', hits)];
    })).filter(([, count]) => count);
    const next = tally(checked, entry => unique(entry.later.won.map(([name]) => name))).slice(0, 30);
    bars.replaceChildren(element('h5', 'Major awards reached after a festival win'), ...(major.length ? barList(major) : [element('p', 'None on record.', 'meta')]),
      element('h5', 'Awards festival winners won next'), ...barList(next.map(([name, count]) => [name, count, () => filmDialog(name, 'Won after a festival award', checked.filter(entry => entry.later.won.some(([award]) => award === name)).map(entry => entry.film))])));
  }

  // Lists
  const archiveButton = byId('archive-documents');
  let documents = [];
  archiveButton.addEventListener('click', () => {
    open('Archive documents', 'Servants of Knowledge · Internet Archive');
    list('Sources', documents.map(doc => source(doc.url, doc.label)));
  });
  function renderList() {
    const selected = festivalMap.get(festivalId);
    const visibleFestivals = selected ? [selected] : festivals;
    const years = unique(visibleFestivals.flatMap(record => record.editions.map(event => event.year))).sort((a, b) => b - a);
    options(edition, years.map(year => [year, String(year)]), 'All editions');
    edition.parentElement.hidden = view === 'years' || view === 'world';
    const hasFacet = ['films', 'people', 'world'].includes(view);
    byId('facet-label').hidden = !hasFacet;
    byId('kind-label').hidden = view !== 'world';
    if (view === 'world') options(kind, tally(worldFestivals, record => record.types || []).map(([name, count]) => [name, `${name} (${number(count)})`]), 'All types');
    const facetSetup = { people: ['Role', allRoles, 'All roles'], world: ['Region', regions, 'All regions'] }[view] || ['Format', formats, 'All formats'];
    byId('facet-caption').textContent = facetSetup[0];
    options(facet, facetSetup[1].map(value => [value, value]), facetSetup[2]);
    search.placeholder = { films: 'Search titles, names, languages, countries…', people: 'Search people, roles, films…', awards: 'Search awards, winners, films…', years: 'Search years…', across: 'Search people, films…', world: 'Search festivals, cities, countries…' }[view];

    const editionRecord = selected?.editions.find(event => event.year === Number(edition.value));
    const note = byId('edition-note');
    note.replaceChildren();
    if (editionRecord?.catalogue) note.append(source(editionRecord.catalogue, editionRecord.catalogueLabel || 'Edition catalogue PDF'));
    const archiveLinks = (editionRecord ? [editionRecord] : selected?.editions || []).flatMap(event => (event.archiveDocuments || []).map(doc => ({
      url: doc.url,
      label: doc.name.startsWith('Award winners') ? doc.name : `${event.year} · ${doc.name}`
    })));
    documents = [...new Map(archiveLinks.map(doc => [doc.url, doc])).values()];
    archiveButton.hidden = documents.length === 0;
    const emptyNote = editionRecord?.importedTitles === 0 ? 'This edition’s catalogue is available as a PDF. Indexed titles are still to come.' : 'No matches. Try a different search or filter.';
    results.dataset.empty = emptyNote;

    const query = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    const match = values => query.every(term => normalize(values.flat(Infinity).filter(Boolean).join(' ')).includes(term));
    const matchesEdition = record => (!festivalId || record.festival === festivalId) && (!edition.value || record.year === Number(edition.value));
    if (view === 'world') {
      items = worldFestivals.filter(record => (!facet.value || record.region === facet.value) && (!kind.value || record.types?.includes(kind.value)) && match([record.name, record.short, record.city, record.country, record.region, record.month, record.desc, record.types])).map(record => result([record.region, record.types?.[0], record.since && `since ${record.since}`].filter(Boolean).join(' · '), record.name, [[record.city, record.country].filter(Boolean).join(', '), record.month].filter(Boolean).join(' · '), () => showWorld(record), initials(record.short || record.name), record.logo));
    } else if (view === 'across') {
      // Research view: people who return across festivals or editions, most widely travelled first.
      items = [...people].map(([name, credits]) => {
        const scoped = credits.filter(matchesEdition);
        return { name, scoped, fests: unique(scoped.map(record => record.festival)), editions: unique(scoped.map(label)) };
      }).filter(entry => entry.editions.length > 1 && match([entry.name, entry.scoped.map(record => [record.title, record.role])]))
        .sort((a, b) => b.fests.length - a.fests.length || b.editions.length - a.editions.length || a.name.localeCompare(b.name))
        .map(entry => result(`${entry.fests.length} festival${entry.fests.length === 1 ? '' : 's'} · ${entry.editions.length} editions`, entry.name, unique(entry.scoped.map(record => record.title || record.award[0])).join(' · '), () => showPerson(entry.name), initials(entry.name), portraits[entry.name]));
    } else if (view === 'years') {
      items = selected.editions.filter(event => match([event.year, event.number, event.dates])).map(event => {
        const count = filmsIn(selected.id, event.year).length;
        return result(`${event.number} edition`, `${selected.short} ${event.year}`, [event.dates, count ? `${number(count)} films` : 'Catalogue PDF'].filter(Boolean).join(' · '), () => showEdition(selected, event), String(event.year).slice(2));
      });
    } else if (view === 'people') {
      items = [...people].sort(([a], [b]) => a.localeCompare(b)).flatMap(([name, credits]) => {
        const matching = credits.filter(record => matchesEdition(record) && (!facet.value || record.role === facet.value) && match([name, record.role, record.title, record.award?.[0], label(record)]));
        return matching.length ? [result(unique(matching.map(record => record.role)).join(' · '), name, unique(matching.map(record => record.title || record.award[0])).join(' · '), () => showPerson(name), initials(name), portraits[name])] : [];
      });
    } else if (view === 'awards') {
      items = awards.filter(record => matchesEdition(record) && match([record.award[0], record.award[2], record.title, label(record)])).map(record => result(label(record), record.award[0], [record.award[2], record.title].filter(Boolean).join(' · '), () => showAward(record), '★'));
    } else {
      items = orderedFilms.filter(record => matchesEdition(record) && (!facet.value || record.format === facet.value || (facet.value === ON_YOUTUBE && record.youtube)) && match([record.title, record.format, record.language, record.country, record.section, label(record), record.credits, record.awards.map(([name,, recipient]) => [name, recipient])])).map(record => result(label(record), record.title, filmLine(record), () => showFilm(record), '▶', record.artwork));
    }
    byId('archive-title').textContent = festivalTabs[view] || exploreTabs[view];
    page = 0;
    paginate();
  }
  function paginate() {
    const style = getComputedStyle(results);
    const columns = Number(style.getPropertyValue('--columns'));
    const row = parseFloat(style.gridAutoRows);
    const gap = parseFloat(style.rowGap);
    const rows = Math.max(1, Math.floor((results.clientHeight + gap) / (row + gap)));
    const size = columns * rows;
    pageCount = Math.max(1, Math.ceil(items.length / size));
    page = Math.min(page, pageCount - 1);
    const first = page * size;
    const visible = items.slice(first, first + size);
    results.replaceChildren(...(visible.length ? visible.map(makeCard => makeCard()) : [element('p', results.dataset.empty, 'empty')]));
    byId('count').textContent = items.length ? `${number(first + 1)}–${number(first + visible.length)} of ${number(items.length)}` : '0 results';
    byId('page-status').textContent = `Page ${page + 1} of ${pageCount}`;
    previous.setAttribute('aria-disabled', String(page === 0));
    next.setAttribute('aria-disabled', String(page + 1 === pageCount));
  }

  // Routing: ?f=<festival> picks the festival, #<tab> picks the view.
  function go(id, nextView, resetFilters = true) {
    if (resetFilters) for (const input of [search, edition, facet, kind]) input.value = '';
    festivalId = id;
    view = nextView;
    const url = new URL(location.href);
    if (id) url.searchParams.set('f', id);
    else url.searchParams.delete('f');
    url.hash = nextView === 'home' || (id && nextView === 'discover') ? '' : nextView;
    if (url.href !== location.href) history.pushState(null, '', url);
    render();
  }
  function readLocation() {
    const id = new URLSearchParams(location.search).get('f');
    festivalId = festivalMap.has(id) ? id : '';
    const tab = location.hash.slice(1);
    const tabs = festivalId ? festivalTabs : { ...searchTabs, ...exploreTabs };
    view = Object.hasOwn(tabs, tab) ? tab : festivalId ? 'discover' : 'home';
  }
  function render() {
    const selected = festivalMap.get(festivalId);
    chips.forEach((chip, index) => chip.setAttribute('aria-pressed', String((festivals[index - 1]?.id || '') === festivalId)));
    const line = byId('festival-line');
    line.hidden = !selected;
    if (selected) {
      const img = element('img');
      if (selected.logo) img.src = selected.logo.file;
      img.alt = '';
      const latest = selected.editions[0];
      const official = source(selected.url || selected.source, selected.url ? 'Official site ↗' : 'Source ↗');
      official.className = 'fext';
      line.replaceChildren(...(selected.logo ? [img] : []), element('span', selected.name, 'fn'), element('span', [latest.dates, latest.year].filter(Boolean).join(' '), 'fd'), ...[whenOf(selected)].filter(Boolean).map(whenBadge), official);
    }
    const tabs = selected ? festivalTabs : view === 'home' ? {} : Object.hasOwn(exploreTabs, view) ? exploreTabs : searchTabs;
    byId('tabs').replaceChildren(...Object.entries(tabs).map(([key, text]) => {
      const link = element('a', text);
      link.href = key === 'discover' ? `?f=${festivalId}` : `${selected ? `?f=${festivalId}` : '?'}#${key}`;
      if (key === view) link.setAttribute('aria-current', 'page');
      link.addEventListener('click', event => {
        event.preventDefault();
        go(festivalId, key);
      });
      return link;
    }));
    document.body.dataset.view = view;
    byId('home').hidden = view !== 'home';
    byId('discover').hidden = view !== 'discover';
    byId('archive').hidden = !listViews.includes(view);
    byId('pager').hidden = !listViews.includes(view);
    byId('explore').hidden = !exploreViews.includes(view);
    byId('calendar').hidden = view !== 'calendar';
    if (view === 'home') renderHome();
    else if (view === 'discover') renderDiscover(selected);
    else if (exploreViews.includes(view)) renderExplore();
    else if (view === 'calendar') renderCalendar();
    else renderList();
    document.title = selected ? `${selected.short} · FilmFest Guide` : 'FilmFest Guide';
  }

  for (const input of [search, edition, facet, kind]) input.addEventListener('input', renderList);
  byId('reset').addEventListener('click', () => {
    for (const input of [search, edition, facet, kind]) input.value = '';
    renderList();
  });
  for (const [control, step] of [[previous, -1], [next, 1]]) {
    control.addEventListener('click', () => {
      if (control.getAttribute('aria-disabled') === 'true') return;
      page += step;
      paginate();
    });
  }
  let size = '';
  new ResizeObserver(() => {
    const nextSize = `${results.clientWidth}x${results.clientHeight}`;
    if (nextSize === size || byId('archive').hidden) return;
    size = nextSize;
    paginate();
  }).observe(results);
  window.addEventListener('resize', () => { if (!byId('discover').hidden) fitShelf(); });
  window.addEventListener('popstate', () => {
    readLocation();
    render();
  });
  readLocation();
  render();
}
start().catch(error => {
  console.error(error);
  document.querySelector('.app').append(element('p', 'The catalogue could not load. Refresh to try again.', 'empty'));
});
if ('serviceWorker' in navigator && location.protocol === 'https:') navigator.serviceWorker.register('sw.js');
