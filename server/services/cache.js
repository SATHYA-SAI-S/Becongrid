/**
 * Memory Cache with TTL & Metrics for Overpass, Geocoding, and GDELT
 */
class MemoryCache {
  constructor(defaultTtlMs = 600000) {
    this.defaultTtlMs = defaultTtlMs;
    this.store = new Map();
    this.hits = 0;
    this.misses = 0;
  }

  get(key) {
    const item = this.store.get(key);
    if (!item) {
      this.misses++;
      return null;
    }

    if (Date.now() > item.expiresAt) {
      this.store.delete(key);
      this.misses++;
      return null;
    }

    this.hits++;
    return {
      value: item.value,
      createdAt: item.createdAt,
      ageSeconds: (Date.now() - item.createdAt) / 1000
    };
  }

  set(key, value, ttlMs = this.defaultTtlMs) {
    this.store.set(key, {
      value,
      createdAt: Date.now(),
      expiresAt: Date.now() + ttlMs
    });
  }

  delete(key) {
    return this.store.delete(key);
  }

  clear() {
    this.store.clear();
    this.hits = 0;
    this.misses = 0;
  }

  getStats() {
    return {
      size: this.store.size,
      hits: this.hits,
      misses: this.misses
    };
  }
}

const resourceCache = new MemoryCache();
const geocodeCache = new MemoryCache(86400000); // 24 hours for geocode
const gdeltCache = new MemoryCache(300000); // 5 minutes for GDELT queries

module.exports = {
  MemoryCache,
  resourceCache,
  geocodeCache,
  gdeltCache
};
