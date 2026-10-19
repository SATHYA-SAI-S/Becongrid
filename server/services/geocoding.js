/**
 * Nominatim Geocoding Service with Caching and User-Agent
 */
const https = require('https');
const config = require('../config');
const { geocodeCache } = require('./cache');

async function searchLocations(query) {
  if (!query || !query.trim()) return [];
  const q = query.trim().toLowerCase();

  const cached = geocodeCache.get(q);
  if (cached) return cached.value;

  const url = `${config.NOMINATIM_URL}?format=json&q=${encodeURIComponent(q)}&countrycodes=in&limit=5&addressdetails=1`;

  return new Promise((resolve, reject) => {
    https.get(url, {
      headers: {
        'User-Agent': 'BeaconGrid/2.0 (Emergency Resource Map; Nominatim Client)'
      },
      timeout: 10000
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        if (res.statusCode >= 200 && res.statusCode < 300) {
          try {
            const parsed = JSON.parse(data);
            const results = (parsed || []).map(p => ({
              place_id: p.place_id,
              name: p.name || p.display_name.split(',')[0],
              display_name: p.display_name,
              lat: parseFloat(p.lat),
              lon: parseFloat(p.lon),
              type: p.type,
              importance: p.importance
            }));
            geocodeCache.set(q, results);
            resolve(results);
          } catch (e) {
            resolve([]);
          }
        } else {
          resolve([]);
        }
      });
    }).on('error', () => resolve([])).on('timeout', () => resolve([]));
  });
}

module.exports = {
  searchLocations
};
