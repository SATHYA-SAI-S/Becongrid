// Routing and turn-by-turn fallback manager

import { fetchRoute } from './api.js';

let activeRouteLayer = null;

export function formatDistance(meters) {
  if (meters === undefined || meters === null) return '--';
  if (meters < 1000) {
    return `${Math.round(meters)} m`;
  }
  return `${(meters / 1000).toFixed(1)} km`;
}

export function formatDuration(seconds) {
  if (!seconds) return '--';
  const mins = Math.round(seconds / 60);
  if (mins < 60) {
    return `${mins} min`;
  }
  const hours = Math.floor(mins / 60);
  const remMins = mins % 60;
  return `${hours} hr ${remMins} min`;
}

/**
 * Generate external fallback navigation URLs
 */
export function getNavigationFallbacks(destLat, destLon, destName = '', startLat = null, startLon = null) {
  const encName = encodeURIComponent(destName || 'Emergency Resource');
  
  // Google Maps Universal Link
  let googleMapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${destLat},${destLon}`;
  if (startLat && startLon) {
    googleMapsUrl += `&origin=${startLat},${startLon}`;
  }

  // OpenStreetMap directions
  let osmUrl = `https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&route=`;
  if (startLat && startLon) {
    osmUrl += `${startLat}%2C${startLon}%3B`;
  }
  osmUrl += `${destLat}%2C${destLon}`;

  // Geo URI Scheme (supported natively on Android / iOS navigation apps)
  const geoUri = `geo:${destLat},${destLon}?q=${destLat},${destLon}(${encName})`;

  return {
    googleMapsUrl,
    osmUrl,
    geoUri
  };
}

/**
 * Fetch and draw route on Leaflet map
 */
export async function calculateAndDrawRoute(map, startLat, startLon, destLat, destLon, profile = 'driving') {
  clearRoute(map);

  const routeData = await fetchRoute(startLat, startLon, destLat, destLon, profile);
  
  if (routeData && routeData.geometry && routeData.geometry.coordinates) {
    // GeoJSON coordinates are [lon, lat], Leaflet polyline expects [lat, lon]
    const latLngs = routeData.geometry.coordinates.map(coord => [coord[1], coord[0]]);

    // Draw casing line for high contrast
    const casingLayer = L.polyline(latLngs, {
      color: '#ffffff',
      weight: 8,
      opacity: 0.9,
      lineCap: 'round',
      lineJoin: 'round'
    });

    const routeLayer = L.polyline(latLngs, {
      color: '#2563eb',
      weight: 5,
      opacity: 0.95,
      lineCap: 'round',
      lineJoin: 'round'
    });

    activeRouteLayer = L.featureGroup([casingLayer, routeLayer]).addTo(map);

    // Zoom map to fit route with padding
    map.fitBounds(activeRouteLayer.getBounds(), {
      padding: [80, 80],
      maxZoom: 16
    });
  }

  return routeData;
}

export function clearRoute(map) {
  if (activeRouteLayer && map) {
    map.removeLayer(activeRouteLayer);
    activeRouteLayer = null;
  }
}
