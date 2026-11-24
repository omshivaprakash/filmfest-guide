const byId = id => document.getElementById(id);
const search = byId('search');
const festival = byId('festival');
const edition = byId('edition');
const facet = byId('facet');
const detail = byId('detail');
const content = byId('detail-content');
const results = byId('results');
const views = { films: 'Films', people: 'People', awards: 'Awards' };
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
  const { festivals, films, honors } = await response.json();
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
  const cards = festivals.map(record => {
    const card = button('', 'festival-card', () => {
      festival.value = festival.value === record.id ? '' : record.id;
      edition.value = '';
      search.value = '';
      facet.value = '';
      render();
      byId('archive').scrollIntoView();
    });
    card.append(element('span', record.region.toUpperCase(), 'tag'), element('span', record.name, 'card-title'), element('span', record.description, 'card-copy'));
    return card;
  });
  byId('festival-grid').replaceChildren(...cards);
  options(festival, festivals.map(record => [record.id, record.short]), 'All festivals');

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
    content.append(element('p', [film.language, film.country].filter(Boolean).join(' · '), 'meta'), element('p', film.summary));
    list('Selected credits', film.credits.map(([role, name]) => {
      const row = element('span', `${role} · `);
      row.append(button(name, 'credit-link', () => showPerson(name)));
      return row;
    }));
    list('Awards', film.awards.map(award => source(award[1], [award[0], award[2]].filter(Boolean).join(' · '))));
    list('Sources', [source(event.source, `${event.number} edition · ${event.dates}`), source(record.url, 'Official festival website'), ...film.sources.map((url, index) => source(url, `Film reference ${index + 1}`))]);
  }
  function showPerson(name) {
    open(name, 'PEOPLE');
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
  function result(tag, title, subtitle, action) {
    const card = button('', 'result', action);
    card.append(element('span', tag, 'tag'), element('span', title, 'card-title'), element('span', subtitle, 'card-copy'));
    return card;
  }
  function render() {
    const visibleFestivals = festival.value ? [festivalMap.get(festival.value)] : festivals;
    const years = unique(visibleFestivals.flatMap(record => record.editions.map(event => event.year))).sort((a, b) => b - a);
    options(edition, years.map(year => [year, String(year)]), 'All editions');
    cards.forEach((card, index) => card.setAttribute('aria-pressed', String(festival.value === festivals[index].id)));
    const formats = ['Feature', 'Short film', 'Documentary'];
    const hasFacet = view !== 'awards';
    byId('facet-label').hidden = !hasFacet;
    const choices = view === 'people' ? allRoles : formats;
    byId('facet-caption').textContent = view === 'people' ? 'Role' : 'Format';
    options(facet, choices.map(value => [value, value]), view === 'people' ? 'All roles' : 'All formats');
    const query = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    const match = values => query.every(term => normalize(values.flat(Infinity).filter(Boolean).join(' ')).includes(term));
    const matchesEdition = record => (!festival.value || record.festival === festival.value) && (!edition.value || record.year === Number(edition.value));
    let items;
    if (view === 'people') {
      items = [...people].sort(([a], [b]) => a.localeCompare(b)).flatMap(([name, credits]) => {
        const matching = credits.filter(record => matchesEdition(record) && (!facet.value || record.role === facet.value) && match([name, record.role, record.title, record.award?.[0], label(record)]));
        return matching.length ? [result(unique(matching.map(record => record.role)).join(' · '), name, unique(matching.map(record => record.title || record.award[0])).join(' · '), () => showPerson(name))] : [];
      });
    } else if (view === 'awards') {
      items = awards.filter(record => matchesEdition(record) && match([record.award[0], record.award[2], record.title, label(record)])).map(record => result(label(record), record.award[0], [record.award[2], record.title].filter(Boolean).join(' · '), () => showAward(record)));
    } else {
      items = films.filter(record => matchesEdition(record) && (!facet.value || record.format === facet.value) && match([record.title, record.format, record.language, record.country, label(record), record.credits, record.awards.map(([name,, recipient]) => [name, recipient])])).map(record => result(label(record), record.title, [record.format, record.language, record.country].filter(Boolean).join(' · '), () => showFilm(record)));
    }
    byId('count').textContent = `${items.length} ${items.length === 1 ? 'result' : 'results'}`;
    results.replaceChildren(...(items.length ? items : [element('p', 'No matches. Try a different search or filter.', 'meta')]));
    byId('archive-title').textContent = `Browse ${views[view].toLowerCase()}`;
    for (const link of document.querySelectorAll('nav a')) {
      link.removeAttribute('aria-current');
      if (link.hash === `#${view}`) link.setAttribute('aria-current', 'location');
    }
  }
  function navigate() {
    const section = location.hash.slice(1);
    if (!Object.hasOwn(views, section)) return;
    if (view !== section) {
      view = section;
      facet.value = '';
      render();
    }
    byId('archive').scrollIntoView();
  }
  for (const input of [search, festival, edition, facet]) input.addEventListener('input', render);
  byId('reset').addEventListener('click', () => {
    for (const input of [search, festival, edition, facet]) input.value = '';
    render();
  });
  for (const link of document.querySelectorAll('nav a')) {
    link.addEventListener('click', () => {
      if (location.hash === link.hash) navigate();
    });
  }
  window.addEventListener('hashchange', navigate);
  render();
  navigate();
}
start().catch(() => {
  byId('count').textContent = 'The catalogue could not load. Refresh to try again.';
});
