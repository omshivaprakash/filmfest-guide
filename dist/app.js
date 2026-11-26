const byId = id => document.getElementById(id);
const search = byId('search');
const festival = byId('festival');
const edition = byId('edition');
const facet = byId('facet');
const detail = byId('detail');
const content = byId('detail-content');
const results = byId('results');
const views = { festivals: 'Festivals', films: 'Films', people: 'People', awards: 'Awards' };
let view = 'films';

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
function unique(values) {
  return [...new Set(values)];
}
const normalize = value => value.normalize('NFD').replace(/\p{Diacritic}/gu, '').toLowerCase();

async function start() {
  const response = await fetch('catalog.json');
  if (!response.ok) throw new Error('Catalogue unavailable');
  const { festivals, films, honors, portraits = {} } = await response.json();
  const festivalMap = new Map(festivals.map(record => [record.id, record]));
  const label = record => `${festivalMap.get(record.festival).short} · ${record.year}`;
  const awards = films.flatMap(film => film.awards.map(award => ({ ...film, award, film }))).concat(honors);
  const people = new Map();
  const addCredit = (name, record) => {
    if (!people.has(name)) people.set(name, []);
    people.get(name).push(record);
  };
  for (const film of films) {
    for (const [role, name] of film.credits) addCredit(name, { ...film, role, film });
  }
  for (const honor of honors) addCredit(honor.award[2], honor);
  const allRoles = unique([...people.values()].flat().map(record => record.role)).sort();
  const previous = byId('previous');
  const next = byId('next');
  let items = [];
  let page = 0;
  let pageCount = 1;
  const initialFestival = new URLSearchParams(location.search).get('f');
  festival.value = festivalMap.has(initialFestival) ? initialFestival : '';
  const festivalButtons = ['', ...festivalMap.keys()].map(id => {
    const record = festivalMap.get(id);
    const chip = button(record?.short || 'All festivals', 'festival-chip', () => {
      festival.value = id;
      edition.value = '';
      render();
    });
    if (record?.logo) chip.prepend(thumbnail('', record.logo));
    if (record) chip.title = record.name;
    return chip;
  });
  byId('festival-strip').append(...festivalButtons);
  const orderedFilms = [...films].sort((a, b) => Number(Boolean(b.artwork)) - Number(Boolean(a.artwork)));

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
    open(film.title, `${label(film)} · ${film.format}`);
    if (film.artwork) {
      const figure = element('figure', '', 'film-artwork');
      const caption = element('figcaption', '', 'meta');
      caption.append(source(film.artwork.source, film.artwork.credit));
      figure.append(thumbnail('', film.artwork), caption);
      content.append(figure);
    }
    if (film.language || film.country) content.append(element('p', [film.language, film.country].filter(Boolean).join(' · '), 'meta'));
    if (film.section) content.append(element('p', film.section, 'meta'));
    if (film.summary) content.append(element('p', film.summary));
    if (film.cataloguePage) content.append(element('p', `Catalogue index · printed page ${film.cataloguePage}`, 'meta'));
    list('Selected credits', film.credits.map(([role, name]) => {
      const row = element('span', `${role} · `);
      row.append(button(name, 'credit-link', () => showPerson(name)));
      return row;
    }));
    list('Awards', film.awards.map(award => source(award[1], [award[0], award[2]].filter(Boolean).join(' · '))));
    const editionLabel = [`${event.number} edition`, event.dates].filter(Boolean).join(' · ');
    const references = film.sources.filter(url => url !== event.source);
    list('Sources', [source(event.source, editionLabel), source(record.url, 'Official festival website'), ...references.map((url, index) => source(url, film.fromCatalogue ? 'Film catalogue' : `Film reference ${index + 1}`))]);
  }
  function showPerson(name) {
    open(name, 'PEOPLE');
    const portrait = portraits[name];
    if (portrait) {
      const figure = element('figure', '', 'profile-photo');
      const caption = element('figcaption', '', 'meta');
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
  function thumbnail(fallback, photo) {
    const frame = element('span', fallback, 'thumbnail');
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
  function result(tag, title, subtitle, action, icon = '', photo) {
    return () => {
      const card = button('', 'result', action);
      const copy = element('span', '', 'result-copy');
      copy.append(element('span', tag, 'tag'), element('span', title, 'card-title'), element('span', subtitle, 'card-copy'));
      if (icon || photo) card.append(thumbnail(icon, photo));
      card.append(copy);
      return card;
    };
  }
  function render() {
    const selected = festivalMap.get(festival.value);
    const context = byId('festival-name');
    context.replaceChildren();
    if (selected?.logo) context.append(thumbnail('', selected.logo));
    context.append(element('strong', selected?.name || 'Film festival archive'));
    festivalButtons.forEach((chip, index) => chip.setAttribute('aria-pressed', String((festivals[index - 1]?.id || '') === festival.value)));
    const url = new URL(location.href);
    if (festival.value) url.searchParams.set('f', festival.value);
    else url.searchParams.delete('f');
    if (url.href !== location.href) history.replaceState(null, '', url);
    const visibleFestivals = festival.value ? [festivalMap.get(festival.value)] : festivals;
    const years = unique(visibleFestivals.flatMap(record => record.editions.map(event => event.year))).sort((a, b) => b - a);
    options(edition, years.map(year => [year, String(year)]), 'All editions');
    const formats = unique(films.map(film => film.format)).sort();
    const editionRecord = visibleFestivals.length === 1 && visibleFestivals[0].editions.find(record => record.year === Number(edition.value));
    const note = byId('edition-note');
    note.dataset.status = editionRecord?.importedTitles === 0 ? 'This edition’s catalogue is available as a PDF. Indexed titles are pending.' : '';
    note.replaceChildren(editionRecord?.catalogue ? source(editionRecord.catalogue, editionRecord.catalogueLabel || 'Edition catalogue PDF') : document.createTextNode('Selected editions'));
    const hasFacet = view === 'films' || view === 'people';
    byId('facet-label').hidden = !hasFacet;
    const choices = view === 'people' ? allRoles : formats;
    byId('facet-caption').textContent = view === 'people' ? 'Role' : 'Format';
    options(facet, choices.map(value => [value, value]), view === 'people' ? 'All roles' : 'All formats');
    const query = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    const match = values => query.every(term => normalize(values.flat(Infinity).filter(Boolean).join(' ')).includes(term));
    const matchesEdition = record => (!festival.value || record.festival === festival.value) && (!edition.value || record.year === Number(edition.value));
    if (view === 'festivals') {
      items = visibleFestivals.filter(record => record.editions.some(event => !edition.value || event.year === Number(edition.value)) && match([record.name, record.short, record.region, record.editions.map(event => event.year)])).map(record => result(record.region, record.name, record.description, () => {
        search.value = '';
        festival.value = record.id;
        location.hash = 'films';
      }, '', record.logo));
    } else if (view === 'people') {
      items = [...people].sort(([a], [b]) => a.localeCompare(b)).flatMap(([name, credits]) => {
        const matching = credits.filter(record => matchesEdition(record) && (!facet.value || record.role === facet.value) && match([name, record.role, record.title, record.award?.[0], label(record)]));
        return matching.length ? [result(unique(matching.map(record => record.role)).join(' · '), name, unique(matching.map(record => record.title || record.award[0])).join(' · '), () => showPerson(name), name.split(/\s+/).slice(0, 2).map(part => part[0]).join(''), portraits[name])] : [];
      });
    } else if (view === 'awards') {
      items = awards.filter(record => matchesEdition(record) && match([record.award[0], record.award[2], record.title, label(record)])).map(record => result(label(record), record.award[0], [record.award[2], record.title].filter(Boolean).join(' · '), () => showAward(record)));
    } else {
      items = orderedFilms.filter(record => matchesEdition(record) && (!facet.value || record.format === facet.value) && match([record.title, record.format, record.language, record.country, record.section, label(record), record.credits, record.awards.map(([name,, recipient]) => [name, recipient])])).map(record => result(label(record), record.title, [record.format, record.language, record.country].filter(Boolean).join(' · '), () => showFilm(record), '▤', record.artwork));
    }
    document.body.dataset.view = view;
    byId('archive-title').textContent = views[view];
    page = 0;
    paginate();
    for (const link of document.querySelectorAll('nav a')) {
      link.removeAttribute('aria-current');
      if (link.hash === `#${view}`) link.setAttribute('aria-current', 'location');
    }
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
    const start = page * size;
    const visible = items.slice(start, start + size);
    if (visible.length) {
      results.replaceChildren(...visible.map(makeCard => makeCard()));
    } else {
      results.replaceChildren(element('p', byId('edition-note').dataset.status || 'No matches. Try a different search or filter.', 'meta'));
    }
    byId('count').textContent = items.length ? `${start + 1}–${start + visible.length} of ${items.length}` : '0 results';
    byId('page-status').textContent = `Page ${page + 1} of ${pageCount}`;
    previous.setAttribute('aria-disabled', String(page === 0));
    next.setAttribute('aria-disabled', String(page + 1 === pageCount));
  }
  function navigate() {
    const section = location.hash.slice(1);
    const selectedView = Object.hasOwn(views, section) ? section : 'films';
    if (view === selectedView) return;
    view = selectedView;
    facet.value = '';
    render();
  }
  for (const input of [search, festival, edition, facet]) input.addEventListener('input', render);
  byId('reset').addEventListener('click', () => {
    for (const input of [search, festival, edition, facet]) input.value = '';
    render();
  });
  for (const [control, step] of [[previous, -1], [next, 1]]) {
    control.addEventListener('click', () => {
      if (control.getAttribute('aria-disabled') === 'true') return;
      page += step;
      paginate();
    });
  }
  let resultWidth = results.clientWidth;
  let resultHeight = results.clientHeight;
  new ResizeObserver(() => {
    if (resultWidth === results.clientWidth && resultHeight === results.clientHeight) return;
    resultWidth = results.clientWidth;
    resultHeight = results.clientHeight;
    paginate();
  }).observe(results);
  window.addEventListener('hashchange', navigate);
  render();
  navigate();
}
start().catch(() => {
  byId('count').textContent = 'The catalogue could not load. Refresh to try again.';
});
