/**
 * Overpass API Service with Multi-Server Fallback & Normalization
 */
const https = require('https');
const { resourceCache } = require('./cache');
const config = require('../config');

// Category mapping from OSM tags
const AMENITY_CATEGORY_MAP = {
  hospital: 'hospital',
  clinic: 'clinic',
  doctors: 'clinic',
  pharmacy: 'pharmacy',
  fire_station: 'fire_station',
  police: 'police',
  shelter: 'shelter',
  drinking_water: 'drinking_water',
  toilets: 'toilets',
  food_bank: 'food_bank',
  social_facility: 'shelter'
};

function calculateDistanceMeters(lat1, lon1, lat2, lon2) {
  const R = 6371000; // Earth radius in meters
  const dLat = (lat2 - lat1) * Math.PI / 180;
  const dLon = (lon2 - lon1) * Math.PI / 180;
  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
    Math.sin(dLon / 2) * Math.sin(dLon / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return Math.round(R * c);
}

function normalizeElement(elem, centerLat, centerLon) {
  const tags = elem.tags || {};
  const lat = elem.lat !== undefined ? elem.lat : (elem.center ? elem.center.lat : null);
  const lon = elem.lon !== undefined ? elem.lon : (elem.center ? elem.center.lon : null);

  if (lat === null || lon === null) return null;

  const rawAmenity = tags.amenity || tags.emergency || tags.social_facility || 'emergency_facility';
  const category = AMENITY_CATEGORY_MAP[rawAmenity] || 'emergency_facility';

  const name = tags.name || tags['name:en'] || tags['name:ta'] || null;
  const phone = tags.phone || tags['contact:phone'] || tags['emergency:phone'] || null;
  const openingHours = tags.opening_hours || null;

  // Address assembly
  const street = tags['addr:street'] || '';
  const housenumber = tags['addr:housenumber'] || '';
  const city = tags['addr:city'] || tags['addr:suburb'] || '';
  const postcode = tags['addr:postcode'] || '';
  const addressParts = [housenumber, street, city, postcode].filter(Boolean);
  const address = addressParts.length > 0 ? addressParts.join(', ') : null;

  const distanceMeters = calculateDistanceMeters(centerLat, centerLon, lat, lon);

  return {
    id: `${elem.type}/${elem.id}`,
    osm_type: elem.type,
    osm_id: elem.id,
    name: name,
    category: category,
    lat: lat,
    lon: lon,
    address: address,
    phone: phone,
    opening_hours: openingHours,
    wheelchair: tags.wheelchair || null,
    emergency_service: tags.emergency === 'yes' || category === 'hospital',
    distance_meters: distanceMeters,
    raw_tags: tags
  };
}

function buildOverpassQuery(lat, lon, radius, categories = []) {
  const selectedCategories = categories.length > 0
    ? categories
    : ['hospital', 'clinic', 'pharmacy', 'fire_station', 'police', 'shelter', 'drinking_water'];

  const amenityFilters = selectedCategories.map(c => `node["amenity"="${c}"](around:${radius},${lat},${lon});\n  way["amenity"="${c}"](around:${radius},${lat},${lon});`).join('\n  ');

  return `[out:json][timeout:25];
(
  ${amenityFilters}
);
out center body;
>;
out skel qt;`;
}

async function queryOverpassServer(serverUrl, query) {
  return new Promise((resolve, reject) => {
    const postData = `data=${encodeURIComponent(query)}`;
    const urlObj = new URL(serverUrl);

    const options = {
      hostname: urlObj.hostname,
      port: urlObj.port || 443,
      path: urlObj.pathname,
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': Buffer.byteLength(postData),
        'User-Agent': 'BeaconGrid/2.0 (Emergency Resource Map; Node.js)'
      },
      timeout: 25000
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        if (res.statusCode >= 200 && res.statusCode < 300) {
          try {
            const parsed = JSON.parse(data);
            resolve(parsed.elements || []);
          } catch (e) {
            reject(new Error(`Invalid JSON from ${urlObj.hostname}`));
          }
        } else {
          reject(new Error(`HTTP ${res.statusCode} from ${urlObj.hostname}`));
        }
      });
    });

    req.on('error', reject);
    req.on('timeout', () => {
      req.destroy();
      reject(new Error(`Timeout from ${urlObj.hostname}`));
    });

    req.write(postData);
    req.end();
  });
}

async function queryOverpassWithFallback(lat, lon, radius, categories = []) {
  const query = buildOverpassQuery(lat, lon, radius, categories);
  let lastErr = null;

  for (const server of config.OVERPASS_SERVERS) {
    try {
      const elements = await queryOverpassServer(server, query);
      return { elements, server };
    } catch (err) {
      lastErr = err;
      console.warn(`Upstream Overpass server ${server} failed: ${err.message}. Trying next fallback...`);
    }
  }

  throw new Error(`All upstream Overpass servers failed. Last error: ${lastErr ? lastErr.message : 'Unknown'}`);
}

async function getResources({ lat, lon, radius = 5000, categories = [] }) {
  const catKey = categories.sort().join(',');
  const cacheKey = `res_${lat.toFixed(3)}_${lon.toFixed(3)}_${radius}_${catKey}`;

  const cached = resourceCache.get(cacheKey);
  if (cached) {
    return {
      data: cached.value,
      count: cached.value.length,
      meta: {
        cached: true,
        cache_age_seconds: cached.ageSeconds,
        timestamp: new Date(cached.createdAt).toISOString()
      }
    };
  }

  const { elements, server } = await queryOverpassWithFallback(lat, lon, radius, categories);

  const normalizedList = elements
    .map(el => normalizeElement(el, lat, lon))
    .filter(Boolean);

  // Deduplicate by id and sort by distance
  const uniqueMap = new Map();
  normalizedList.forEach(item => {
    if (!uniqueMap.has(item.id)) {
      uniqueMap.set(item.id, item);
    }
  });

  const sortedResults = Array.from(uniqueMap.values()).sort((a, b) => a.distance_meters - b.distance_meters);

  resourceCache.set(cacheKey, sortedResults);

  return {
    data: sortedResults,
    count: sortedResults.length,
    meta: {
      cached: false,
      upstream_server: new URL(server).hostname,
      timestamp: new Date().toISOString()
    }
  };
}

module.exports = {
  getResources,
  queryOverpassWithFallback,
  normalizeElement,
  calculateDistanceMeters
};
