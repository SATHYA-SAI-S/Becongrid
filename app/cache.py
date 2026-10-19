"""In-memory TTL cache with telemetry and thread safety."""
import time
import threading
from typing import Any, Optional, Tuple

class SimpleTtlCache:
    """Thread-safe in-memory cache with expiration timestamps and telemetry."""
    def __init__(self, default_ttl_seconds: int = 600):
        self.default_ttl = default_ttl_seconds
        self._cache = {} # key -> (data, expires_at, created_at)
        self._lock = threading.Lock()
        self.hits = 0
        self.misses = 0

    def get(self, key: str) -> Optional[Tuple[Any, float]]:
        """
        Retrieve cached value.
        Returns (data, age_in_seconds) or None if expired/not found.
        """
        now = time.time()
        with self._lock:
            if key not in self._cache:
                self.misses += 1
                return None

            data, expires_at, created_at = self._cache[key]
            if now > expires_at:
                del self._cache[key]
                self.misses += 1
                return None

            self.hits += 1
            age = now - created_at
            return (data, age)

    def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> None:
        """Store value in cache with expiration."""
        ttl = ttl_seconds if ttl_seconds is not None else self.default_ttl
        now = time.time()
        with self._lock:
            # Simple eviction if cache grows beyond 1000 items
            if len(self._cache) > 1000:
                self._evict_expired(now)

            self._cache[key] = (value, now + ttl, now)

    def _evict_expired(self, now: float) -> None:
        """Remove expired entries."""
        expired_keys = [k for k, (_, exp, _) in self._cache.items() if now > exp]
        for k in expired_keys:
            del self._cache[k]
        # If still over 800 items, clear oldest 200
        if len(self._cache) > 800:
            sorted_keys = sorted(self._cache.keys(), key=lambda k: self._cache[k][2])
            for k in sorted_keys[:200]:
                del self._cache[k]

    def clear(self) -> None:
        """Clear all entries."""
        with self._lock:
            self._cache.clear()

# Global cache singletons
resource_cache = SimpleTtlCache(default_ttl_seconds=600)
geocode_cache = SimpleTtlCache(default_ttl_seconds=86400)
route_cache = SimpleTtlCache(default_ttl_seconds=3600)
