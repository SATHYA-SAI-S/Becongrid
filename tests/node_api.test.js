/**
 * Node.js Native Integration & Unit Tests for BeaconGrid API
 * Covers Overpass, Routing, Geocoding, GDELT Classification, MongoDB/Storage, and Ingestion
 */
const { test, describe, before, after } = require('node:test');
const assert = require('node:assert');
const http = require('http');
const { app } = require('../server');
const { gdeltService } = require('../server/services/gdelt');
const { storage } = require('../server/db/storage');
const { getNavigationFallbacks } = require('../server/services/routing');

let serverInstance = null;
let baseUrl = '';

before(async () => {
  return new Promise((resolve) => {
    serverInstance = app.listen(0, '127.0.0.1', () => {
      const port = serverInstance.address().port;
      baseUrl = `http://127.0.0.1:${port}`;
      resolve();
    });
  });
});

after(async () => {
  return new Promise((resolve) => {
    if (serverInstance) {
      serverInstance.close(resolve);
    } else {
      resolve();
    }
  });
});

function requestGet(path) {
  return new Promise((resolve, reject) => {
    http.get(`${baseUrl}${path}`, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        let json = null;
        try { json = JSON.parse(data); } catch (e) {}
        resolve({
          statusCode: res.statusCode,
          headers: res.headers,
          body: data,
          json: json
        });
      });
    }).on('error', reject);
  });
}

function requestPost(path, bodyObj) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify(bodyObj || {});
    const urlObj = new URL(`${baseUrl}${path}`);
    const req = http.request({
      hostname: urlObj.hostname,
      port: urlObj.port,
      path: urlObj.pathname,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        let json = null;
        try { json = JSON.parse(data); } catch (e) {}
        resolve({
          statusCode: res.statusCode,
          headers: res.headers,
          body: data,
          json: json
        });
      });
    });
    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

describe('BeaconGrid Node.js API Endpoints', () => {
  test('GET / serves landing page HTML', async () => {
    const res = await requestGet('/');
    assert.strictEqual(res.statusCode, 200);
    assert.ok(res.body.includes('BeaconGrid'));
    assert.ok(res.body.includes('<!DOCTYPE html>'));
  });

  test('GET /map.html serves map dashboard HTML', async () => {
    const res = await requestGet('/map.html');
    assert.strictEqual(res.statusCode, 200);
    assert.ok(res.body.includes('BeaconGrid Live Map'));
    assert.ok(res.body.includes('leafletMap'));
  });

  test('GET /api/health returns healthy status and database metrics', async () => {
    const res = await requestGet('/api/health');
    assert.strictEqual(res.statusCode, 200);
    assert.strictEqual(res.json.status, 'healthy');
    assert.ok(res.json.database);
    assert.ok(res.json.intelligence);
  });

  test('GET /api/resources validates missing and out-of-range parameters', async () => {
    // Missing lat/lon
    const res1 = await requestGet('/api/resources');
    assert.strictEqual(res1.statusCode, 422);

    // Invalid latitude
    const res2 = await requestGet('/api/resources?lat=95.0&lon=80.2');
    assert.strictEqual(res2.statusCode, 422);

    // Radius too large (> 10000m)
    const res3 = await requestGet('/api/resources?lat=13.08&lon=80.27&radius=50000');
    assert.strictEqual(res3.statusCode, 422);
  });

  test('GET /api/geocode returns geocoding structure', async () => {
    const res = await requestGet('/api/geocode?q=Chennai');
    assert.strictEqual(res.statusCode, 200);
    assert.strictEqual(res.json.status, 'ok');
    assert.ok(Array.isArray(res.json.results));
  });

  test('GET /api/route validates parameters and provides navigation fallbacks', async () => {
    const res = await requestGet('/api/route?start_lat=13.08&start_lon=80.27&end_lat=13.05&end_lon=80.25');
    assert.strictEqual(res.statusCode, 200);
    assert.ok(res.json.fallbacks);
    assert.ok(res.json.fallbacks.google_maps.includes('13.05,80.25'));
    assert.ok(res.json.fallbacks.openstreetmap);
  });

  test('GET /api/incidents returns news-derived incidents with metadata and GeoJSON', async () => {
    const res = await requestGet('/api/incidents');
    assert.strictEqual(res.statusCode, 200);
    assert.strictEqual(res.json.status, 'ok');
    assert.ok(res.json.count >= 1);
    assert.ok(Array.isArray(res.json.data));
    
    // Check GeoJSON point format on first incident
    const first = res.json.data[0];
    assert.ok(first.incidentId);
    assert.ok(first.category);
    assert.strictEqual(first.location.type, 'Point');
    assert.strictEqual(first.location.coordinates.length, 2);
    assert.ok(first.verificationStatus);
  });

  test('GET /api/incidents filters by category and district', async () => {
    const res = await requestGet('/api/incidents?category=natural_disaster&district=tirunelveli');
    assert.strictEqual(res.statusCode, 200);
    assert.ok(res.json.data.length >= 1);
    res.json.data.forEach(inc => {
      assert.strictEqual(inc.category, 'natural_disaster');
      assert.strictEqual(inc.district, 'tirunelveli');
    });
  });

  test('GET /api/incidents/:id returns single incident and supporting articles', async () => {
    const res = await requestGet('/api/incidents/inc-tn-fld-01');
    assert.strictEqual(res.statusCode, 200);
    assert.strictEqual(res.json.incident.incidentId, 'inc-tn-fld-01');
    assert.ok(Array.isArray(res.json.articles));
    assert.ok(res.json.articles.length >= 1);
  });

  test('POST /api/incidents/refresh returns controlled cycle status', async () => {
    const res = await requestPost('/api/incidents/refresh', {});
    assert.strictEqual(res.statusCode, 200);
    assert.ok(res.json.status === 'success' || res.json.status === 'completed_with_upstream_notice' || res.json.status === 'already_running');
    assert.ok(res.json.stats);
  });

  test('POST /api/incidents/report-issue flags unverified incidents as disputed', async () => {
    const res = await requestPost('/api/incidents/report-issue', {
      incidentId: 'inc-tn-fir-03',
      issueType: 'disputed_location',
      comments: 'Fire was in adjacent ward not main industrial block.'
    });
    assert.strictEqual(res.statusCode, 200);
    assert.strictEqual(res.json.status, 'ok');

    // Verify incident was updated
    const updated = await storage.getIncidentById('inc-tn-fir-03');
    assert.strictEqual(updated.verificationStatus, 'disputed');
  });
});

describe('GDELT Intelligence Classification & Location Extraction', () => {
  test('classifyArticle accurately identifies natural disasters and fires', () => {
    const res1 = gdeltService.classifyArticle('Massive flood and inundation after heavy rain in Cuddalore', 'River breached banks');
    assert.strictEqual(res1.category, 'natural_disaster');

    const res2 = gdeltService.classifyArticle('Fire outbreak in garment packaging godown', 'Fire tenders deployed');
    assert.strictEqual(res2.category, 'accident_emergency');

    const res3 = gdeltService.classifyArticle('Farmers road roko and rally against power tariffs', 'Traffic halted on highway');
    assert.strictEqual(res3.category, 'protest_disturbance');
  });

  test('extractLocation identifies Tamil Nadu districts and towns with coordinate mapping', () => {
    const loc1 = gdeltService.extractLocation('Landslide on Coonoor ghat road near Marapalam', 'Traffic halted');
    assert.ok(loc1);
    assert.strictEqual(loc1.district, 'nilgiris');
    assert.strictEqual(loc1.city, 'Coonoor');
    assert.strictEqual(loc1.precision, 'exact');

    const loc2 = gdeltService.extractLocation('Heavy waterlogging reported across Madurai district', 'Vaigai river swollen');
    assert.ok(loc2);
    assert.strictEqual(loc2.district, 'madurai');
    assert.strictEqual(loc2.precision, 'city');
  });

  test('generateFingerprint creates reproducible SHA-256 hashes for deduplication', () => {
    const f1 = gdeltService.generateFingerprint('Headline One', 'The Hindu', '2026-10-19T10:00:00Z');
    const f2 = gdeltService.generateFingerprint('Headline One', 'The Hindu', '2026-10-19T10:00:00Z');
    const f3 = gdeltService.generateFingerprint('Headline Two', 'The Hindu', '2026-10-19T10:00:00Z');

    assert.strictEqual(f1, f2);
    assert.notStrictEqual(f1, f3);
  });
});
