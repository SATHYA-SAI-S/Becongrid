"""Tests for the thread-safe TTL cache."""
import time
from app.cache import SimpleTtlCache

def test_cache_set_and_get():
    cache = SimpleTtlCache(default_ttl_seconds=10)
    cache.set("key1", {"msg": "hello"})

    result = cache.get("key1")
    assert result is not None
    data, age = result
    assert data == {"msg": "hello"}
    assert age >= 0.0
    assert cache.hits == 1
    assert cache.misses == 0

def test_cache_miss():
    cache = SimpleTtlCache(default_ttl_seconds=10)
    result = cache.get("nonexistent")
    assert result is None
    assert cache.hits == 0
    assert cache.misses == 1

def test_cache_expiration():
    # Cache with 0.1 second TTL
    cache = SimpleTtlCache(default_ttl_seconds=1)
    cache.set("short_key", "temporary", ttl_seconds=0) # Expired immediately
    time.sleep(0.01)

    result = cache.get("short_key")
    assert result is None
    assert cache.misses == 1

def test_cache_clear():
    cache = SimpleTtlCache()
    cache.set("k1", "v1")
    cache.set("k2", "v2")
    cache.clear()
    assert cache.get("k1") is None
    assert cache.get("k2") is None
