/* Pure projections of CanopyOps native records. No targets or health states are inferred. */
(function (root, factory) {
  'use strict';
  const model = factory();
  if (typeof module === 'object' && module.exports) module.exports = model;
  if (root) root.CanopyModel = model;
}(typeof window === 'object' ? window : null, function () {
  'use strict';

  const nativeFields = 'timestamp,facility,room,zone,crop_id,stage,observer,observation_type,plant_or_sample,observed_condition,severity,distribution,measurement_value,unit,method,sensor_or_tool,photo_or_record,action_taken,incident_id,notes'.split(',');

  function parseCSV(text) {
    const input = String(text == null ? '' : text).replace(/^\uFEFF/, '');
    if (!input) return [];
    const rows = [];
    let row = [], value = '', quoted = false, started = false;
    for (let index = 0; index < input.length; index += 1) {
      const character = input[index];
      if (quoted) {
        if (character === '"') {
          if (input[index + 1] === '"') { value += '"'; index += 1; }
          else quoted = false;
        } else value += character;
      } else if (character === '"' && !started) {
        quoted = true;
        started = true;
      } else if (character === ',') {
        row.push(value);
        value = '';
        started = false;
      } else if (character === '\n' || character === '\r') {
        if (character === '\r' && input[index + 1] === '\n') index += 1;
        row.push(value);
        rows.push(row);
        row = [];
        value = '';
        started = false;
      } else {
        value += character;
        started = true;
      }
    }
    if (quoted) throw new SyntaxError('CSV has an unclosed quoted field. Check the native record.');
    if (started || value || row.length) { row.push(value); rows.push(row); }
    return rows;
  }

  function observations(text) {
    const parsed = parseCSV(text);
    if (!parsed.length) return [];
    const headers = parsed.shift();
    return parsed.map(function (values, index) {
      if (!values.some(value => value.trim() !== '')) return null;
      const row = Object.fromEntries(nativeFields.map(field => [field, '']));
      headers.forEach(function (field, column) {
        // Own properties avoid prototype changes from imported column names.
        if (field) Object.defineProperty(row, field, {
          value: values[column] == null ? '' : values[column],
          enumerable: true, configurable: true, writable: true
        });
      });
      row.id = String(index);
      const time = row.timestamp.trim() ? Date.parse(row.timestamp) : NaN;
      row.time = Number.isFinite(time) ? time : null;
      return row;
    }).filter(Boolean);
  }

  function rooms(rows) {
    return [...new Set(rows.map(row => row.room || '').filter(room => room.trim() !== ''))];
  }

  function zones(rows) {
    return [...new Set(rows.map(row => row.zone && row.zone.trim() ? row.zone : 'Unspecified zone'))];
  }

  function hasMeasurement(row) {
    const value = row.measurement_value;
    return value != null && String(value).trim() !== '' && Number.isFinite(Number(value));
  }

  function series(rows) {
    const grouped = new Map();
    rows.forEach(function (row) {
      // Incomplete or undated readings remain in the source trail and measurement count.
      const requiredContext = ['observation_type', 'unit', 'method', 'sensor_or_tool'];
      if (!hasMeasurement(row) || !Number.isFinite(row.time) ||
          !requiredContext.every(field => String(row[field] == null ? '' : row[field]).trim() !== '')) return;
      const dimensions = ['observation_type', 'unit', 'method', 'sensor_or_tool', 'zone', 'facility', 'room', 'crop_id', 'stage'].map(field => row[field] || '');
      const key = JSON.stringify(dimensions);
      if (!grouped.has(key)) grouped.set(key, {
        key: key,
        label: row.observation_type || 'Unspecified measurement',
        unit: row.unit || '',
        rows: []
      });
      grouped.get(key).rows.push(row);
    });
    return [...grouped.values()].map(function (group) {
      group.rows.sort((left, right) => left.time - right.time);
      return group;
    });
  }

  function summarize(rows) {
    let measured = 0, flagged = 0, latest = null;
    rows.forEach(function (row) {
      if (hasMeasurement(row)) measured += 1;
      if (/^(high|moderate)$/i.test(String(row.severity || '').trim())) flagged += 1;
      if (Number.isFinite(row.time) && (latest === null || row.time > latest)) latest = row.time;
    });
    return { count: rows.length, measured: measured, flagged: flagged, latest: latest };
  }

  function recordSummary(text) {
    const result = {};
    let fenced = false;
    String(text == null ? '' : text).split(/\r?\n/).forEach(function (line) {
      if (/^\s*(```|~~~)/.test(line)) { fenced = !fenced; return; }
      if (fenced) return;
      // Only explicit individual labels. Compound template headings stay in the source.
      line.split(/\s+·\s+/).forEach(function (part) {
        const match = part.match(/^\s*(?:[-*]\s+)?(?:\*\*)?(Room|Batch|Stage|Owner|Status|Next action)(?:\*\*)?\s*:\s*(?:\*\*)?\s*(.*?)\s*$/i);
        if (!match || !match[2]) return;
        const field = match[1].toLowerCase().replace(/\s+/g, '_');
        if (!(field in result)) result[field] = match[2];
      });
    });
    return result;
  }

  return Object.freeze({ parseCSV, observations, rooms, zones, series, summarize, recordSummary });
}));
