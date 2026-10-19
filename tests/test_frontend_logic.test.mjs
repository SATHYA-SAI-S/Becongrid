// Node.js test runner for key frontend logic

import test from 'node:test';
import assert from 'node:assert/strict';

// Import pure functions or replicate for isolated unit verification
function formatDistance(meters) {
  if (meters === undefined || meters === null) return '--';
  if (meters < 1000) {
    return `${Math.round(meters)} m`;
  }
  return `${(meters / 1000).toFixed(1)} km`;
}

function formatDuration(seconds) {
  if (!seconds) return '--';
  const mins = Math.round(seconds / 60);
  if (mins < 60) {
    return `${mins} min`;
  }
  const hours = Math.floor(mins / 60);
  const remMins = mins % 60;
  return `${hours} hr ${remMins} min`;
}

function getNavigationFallbacks(destLat, destLon, destName = '', startLat = null, startLon = null) {
  const encName = encodeURIComponent(destName || 'Emergency Resource');
  let googleMapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${destLat},${destLon}`;
  if (startLat && startLon) {
    googleMapsUrl += `&origin=${startLat},${startLon}`;
  }

  let osmUrl = `https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&route=`;
  if (startLat && startLon) {
    osmUrl += `${startLat}%2C${startLon}%3B`;
  }
  osmUrl += `${destLat}%2C${destLon}`;

  const geoUri = `geo:${destLat},${destLon}?q=${destLat},${destLon}(${encName})`;

  return { googleMapsUrl, osmUrl, geoUri };
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

test('formatDistance formats meters and kilometers accurately', () => {
  assert.equal(formatDistance(0), '0 m');
  assert.equal(formatDistance(450), '450 m');
  assert.equal(formatDistance(999), '999 m');
  assert.equal(formatDistance(1000), '1.0 km');
  assert.equal(formatDistance(3456), '3.5 km');
  assert.equal(formatDistance(null), '--');
});

test('formatDuration formats seconds into minutes and hours', () => {
  assert.equal(formatDuration(0), '--');
  assert.equal(formatDuration(180), '3 min');
  assert.equal(formatDuration(3600), '1 hr 0 min');
  assert.equal(formatDuration(4500), '1 hr 15 min');
});

test('getNavigationFallbacks builds valid Google Maps, OSM, and Geo URI links', () => {
  const links = getNavigationFallbacks(51.5074, -0.1278, 'City Clinic', 51.5000, -0.1200);
  assert.ok(links.googleMapsUrl.includes('destination=51.5074,-0.1278'));
  assert.ok(links.googleMapsUrl.includes('origin=51.5,-0.12'));
  assert.ok(links.osmUrl.includes('51.5%2C-0.12%3B51.5074%2C-0.1278'));
  assert.ok(links.geoUri.startsWith('geo:51.5074,-0.1278'));
  assert.ok(links.geoUri.includes('City%20Clinic'));
});

test('escapeHtml prevents XSS injections in place names and hours', () => {
  const dangerous = '<script>alert("xss")</script> & "quotes"';
  const safe = escapeHtml(dangerous);
  assert.equal(safe, '&lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt; &amp; &quot;quotes&quot;');
});

test('race condition prevention: only latest sequence ID is accepted', () => {
  let latestSeq = 0;
  const processed = [];

  function simulateResponse(seq, data) {
    if (seq === latestSeq) {
      processed.push(data);
    }
  }

  // Request 1 starts
  const seq1 = ++latestSeq;
  // Request 2 starts before request 1 finishes
  const seq2 = ++latestSeq;

  // Request 1 arrives late
  simulateResponse(seq1, 'stale_result');
  // Request 2 arrives
  simulateResponse(seq2, 'fresh_result');

  assert.deepEqual(processed, ['fresh_result']);
});
