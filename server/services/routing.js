/**
 * OSRM Routing Service with Navigation Fallbacks
 */
const https = require('https');
const config = require('../config');

function getNavigationFallbacks(destLat, destLon, originLat = null, originLon = null) {
  let googleMapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${destLat},${destLon}`;
  if (originLat !== null && originLon !== null) {
    googleMapsUrl += `&origin=${originLat},${originLon}`;
  }

  let osmUrl = `https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&route=`;
  if (originLat !== null && originLon !== null) {
    osmUrl += `${originLat}%2C${originLon}%3B${destLat}%2C${destLon}`;
  } else {
    osmUrl = `https://www.openstreetmap.org/?mlat=${destLat}&mlon=${destLon}#map=16/${destLat}/${destLon}`;
  }

  const geoUri = `geo:${destLat},${destLon}?q=${destLat},${destLon}`;

  return {
    google_maps: googleMapsUrl,
    openstreetmap: osmUrl,
    geo_uri: geoUri
  };
}

async function getRoute(startLat, startLon, endLat, endLon) {
  const fallbacks = getNavigationFallbacks(endLat, endLon, startLat, startLon);
  const url = `${config.OSRM_URL}/${startLon},${startLat};${endLon},${endLat}?overview=full&geometries=geojson`;

  return new Promise((resolve) => {
    https.get(url, { timeout: 10000 }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        if (res.statusCode === 200) {
          try {
            const parsed = JSON.parse(data);
            if (parsed.routes && parsed.routes.length > 0) {
              const route = parsed.routes[0];
              return resolve({
                status: 'ok',
                distance_meters: Math.round(route.distance),
                duration_seconds: Math.round(route.duration),
                geometry: route.geometry,
                disclaimer: 'Route provided for reference only. Verify road conditions with local authorities in emergencies.',
                fallbacks: fallbacks
              });
            }
          } catch (e) {}
        }

        // Fallback response if OSRM fails
        resolve({
          status: 'routing_unavailable',
          message: 'Direct routing endpoint is currently unreachable. Use external navigation fallback.',
          fallbacks: fallbacks
        });
      });
    }).on('error', () => {
      resolve({
        status: 'routing_unavailable',
        message: 'Direct routing endpoint unreachable. Use external navigation fallback.',
        fallbacks: fallbacks
      });
    }).on('timeout', () => {
      resolve({
        status: 'routing_unavailable',
        message: 'Routing request timed out. Use external navigation fallback.',
        fallbacks: fallbacks
      });
    });
  });
}

module.exports = {
  getRoute,
  getNavigationFallbacks
};
