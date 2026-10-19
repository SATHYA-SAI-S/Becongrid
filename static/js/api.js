// API Client with race condition prevention and error handling

import { CONFIG } from './config.js';

let currentResourceAbortController = null;
let latestRequestSeq = 0;

let currentGeocodeAbortController = null;

export class ApiError extends Error {
  constructor(message, status = 500, details = null) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
    this.details = details;
  }
}

/**
 * Fetch emergency resources around a point
 * Automatically cancels previous in-flight requests and ignores stale responses
 */
export async function fetchResources({ lat, lon, radius = CONFIG.DEFAULT_RADIUS_METERS, categories = [] }) {
  // Cancel previous request if still running
  if (currentResourceAbortController) {
    currentResourceAbortController.abort();
  }
  currentResourceAbortController = new AbortController();
  const signal = currentResourceAbortController.signal;

  const thisRequestSeq = ++latestRequestSeq;

  const params = new URLSearchParams({
    lat: lat.toFixed(6),
    lon: lon.toFixed(6),
    radius: Math.round(radius).toString()
  });

  if (categories && categories.length > 0) {
    params.set('categories', categories.join(','));
  }

  try {
    const url = `${CONFIG.API_RESOURCES}?${params.toString()}`;
    const response = await fetch(url, { signal });

    if (!response.ok) {
      let errPayload = {};
      try {
        errPayload = await response.json();
      } catch (_) {}
      throw new ApiError(
        errPayload.detail || errPayload.message || `Upstream service returned error (${response.status})`,
        response.status,
        errPayload
      );
    }

    const data = await response.json();

    // Guard against race conditions: verify this is still the newest request
    if (thisRequestSeq !== latestRequestSeq) {
      const staleError = new Error('Stale response discarded');
      staleError.name = 'AbortError';
      throw staleError;
    }

    return data;
  } catch (err) {
    if (err.name === 'AbortError') {
      throw err; // rethrow aborts silently
    }
    if (err instanceof ApiError) {
      throw err;
    }
    throw new ApiError(`Network request failed: ${err.message}`, 0, err);
  } finally {
    if (thisRequestSeq === latestRequestSeq) {
      currentResourceAbortController = null;
    }
  }
}

/**
 * Search locations via geocoding proxy
 */
export async function geocodeSearch(query, { lat, lon } = {}) {
  if (!query || query.trim().length < 2) {
    return [];
  }

  if (currentGeocodeAbortController) {
    currentGeocodeAbortController.abort();
  }
  currentGeocodeAbortController = new AbortController();

  const params = new URLSearchParams({ q: query.trim() });
  if (lat !== undefined && lon !== undefined) {
    params.set('lat', lat.toString());
    params.set('lon', lon.toString());
  }

  try {
    const response = await fetch(`${CONFIG.API_GEOCODE}?${params.toString()}`, {
      signal: currentGeocodeAbortController.signal
    });
    if (!response.ok) return [];
    const data = await response.json();
    return data.results || [];
  } catch (err) {
    if (err.name === 'AbortError') return [];
    console.warn('Geocoding request failed:', err);
    return [];
  }
}

/**
 * Calculate route between start and destination
 */
export async function fetchRoute(startLat, startLon, destLat, destLon, profile = 'driving') {
  const params = new URLSearchParams({
    start_lat: startLat.toFixed(6),
    start_lon: startLon.toFixed(6),
    dest_lat: destLat.toFixed(6),
    dest_lon: destLon.toFixed(6),
    profile
  });

  try {
    const response = await fetch(`${CONFIG.API_ROUTE}?${params.toString()}`);
    if (!response.ok) {
      let errPayload = {};
      try { errPayload = await response.json(); } catch (_) {}
      throw new ApiError(errPayload.detail || 'Failed to calculate route', response.status);
    }
    return await response.json();
  } catch (err) {
    if (err instanceof ApiError) throw err;
    throw new ApiError(`Routing network error: ${err.message}`, 0);
  }
}
