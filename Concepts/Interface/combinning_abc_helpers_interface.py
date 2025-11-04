"""
Exercise ------ 6 -------- Combining ABC and Concrete Helpers

Build an abstract base class CacheBackend that declares an abstract method get(key: str) -> Any and set(key: str, value: Any) -> None. 
Add a concrete helper method clear() that removes all stored keys (you can store data in a protected dict _store).

Implement two subclasses:
    InMemoryCache that keeps data in a regular dictionary.
    FileCache that persists each key/value pair as a separate JSON file under a given directory.

Write a short demo that creates both caches, sets a few values, 
retrieves them, calls clear(), and shows that the caches are empty afterwards.

Hints
    Use json.dump/json.load for the file-based cache.
    The concrete clear method can simply self._store.clear() for the in-memory version and delete all files for the file 
    version (you may override clear in FileCache if you need filesystem cleanup).
"""
