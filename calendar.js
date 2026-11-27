// Festival calendar: whether a festival is on now, over, or coming next, worked out from today's date in the browser.
// Exact dates come from editions ("20–28 November" + year); otherwise a usual month ("October–November") or the last
// edition's dates give an estimate, which is always labelled "usually" so no date is invented.
const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

function editionRange(event) {
  const match = /^(\d{1,2})(?: ([A-Z][a-z]+))?–(\d{1,2}) ([A-Z][a-z]+)$/.exec(event?.dates || '');
  if (!match || !event.year) return null;
  const endMonth = MONTHS.indexOf(match[4]);
  const startMonth = match[2] ? MONTHS.indexOf(match[2]) : endMonth;
  if (startMonth < 0 || endMonth < 0) return null;
  return [new Date(event.year, startMonth, +match[1]), new Date(event.year + (endMonth < startMonth ? 1 : 0), endMonth, +match[3])];
}

const short = date => `${date.getDate()} ${MONTHS[date.getMonth()].slice(0, 3)}`;
const rangeText = ([start, end]) => `${start.getMonth() === end.getMonth() ? start.getDate() : short(start)}–${short(end)} ${end.getFullYear()}`;
const monthsText = (first, last) => (first === last ? MONTHS[first] : `${MONTHS[first]}–${MONTHS[last]}`);

// Returns { status: 'now' | 'month' | 'next' | 'over', sure, text, brief, start, end } or null when nothing is known.
// 'month' means "usually held about now" without confirmed dates. start is the next (or current) start, for sorting;
// end is when the current or most recent run ends.
function festivalWhen(record, today = new Date()) {
  today = new Date(today.getFullYear(), today.getMonth(), today.getDate());
  const year = today.getFullYear();
  // World festivals carry an edition count (data/enrich), not a list; only guide festivals have dated editions.
  const ranges = (Array.isArray(record.editions) ? record.editions : []).map(editionRange).filter(Boolean).sort((a, b) => a[0] - b[0]);
  const now = ranges.find(([start, end]) => start <= today && today <= end);
  if (now) return { status: 'now', sure: true, text: `On now · until ${short(now[1])}`, brief: `until ${short(now[1])}`, start: now[0], end: now[1] };
  const coming = ranges.find(([start]) => start > today);
  if (coming) return { status: 'next', sure: true, text: `Next: ${rangeText(coming)}`, brief: rangeText(coming), start: coming[0], end: coming[1] };
  const last = ranges.at(-1);
  // The usual pattern: the last edition's days, else the usual month(s).
  let first, lastMonth, startDay = 1, endDay;
  if (last) [first, startDay, lastMonth, endDay] = [last[0].getMonth(), last[0].getDate(), last[1].getMonth(), last[1].getDate()];
  else {
    const named = MONTHS.map((name, index) => [String(record.month || '').indexOf(name), index]).filter(([at]) => at >= 0).sort((a, b) => a[0] - b[0]).map(([, index]) => index);
    if (!named.length) return null;
    [first, lastMonth] = [named[0], named.at(-1)];
  }
  const usually = `usually in ${monthsText(first, lastMonth)}`;
  const project = y => [new Date(y, first, startDay), endDay ? new Date(y + (lastMonth < first ? 1 : 0), lastMonth, endDay) : new Date(y + (lastMonth < first ? 1 : 0), lastMonth + 1, 0)];
  const lastTime = last ? ` · last ${rangeText(last)}` : '';
  const off = record.editions?.find?.(event => event.year === year && event.off);
  if (off) return { status: 'over', sure: true, text: `No ${year} edition · ${off.off}`, brief: `no ${year} edition`, start: project(year + 1)[0], end: null };
  if (last && last[0].getFullYear() === year) return { status: 'over', sure: true, text: `Over · ${rangeText(last)}`, brief: `ended ${short(last[1])}`, start: project(year + 1)[0], end: last[1] };
  for (const y of [year - 1, year]) {  // year - 1 catches a December–January run that started last year
    const [start, end] = project(y);
    if (start <= today && today <= end) return { status: 'month', sure: false, text: `Likely on now · ${usually}${lastTime}`, brief: usually, start, end };
  }
  const [start, end] = project(year);
  if (start > today) return { status: 'next', sure: false, text: `${usually[0].toUpperCase()}${usually.slice(1)} · ${year} dates not confirmed`, brief: usually, start, end };
  return { status: 'over', sure: false, text: `Likely over for ${year} · ${usually}`, brief: usually, start: project(year + 1)[0], end };
}

// data/announced/announced.json: hand-checked dates for current editions, merged by festival id. An existing edition keeps
// its own fields and gains the announced ones; datesSource keeps the page the dates came from.
function mergeAnnounced(records, editions = {}) {
  for (const record of records) {
    if (!editions[record.id]) continue;
    const list = Array.isArray(record.editions) ? record.editions : (record.editions = []);
    for (const edition of editions[record.id]) {
      const same = list.find(event => event.year === edition.year);
      if (same) Object.assign(same, { ...edition, ...same, datesSource: edition.source });
      else list.push({ ...edition, datesSource: edition.source });
    }
    list.sort((a, b) => b.year - a.year);
  }
}

if (typeof module === 'object') module.exports = { festivalWhen, mergeAnnounced, MONTHS };
