"""
4) ------ Memoisation (cache) decorator
Build memoize that stores the results of a pure function in a dictionary keyed by the arguments it receives. 
Subsequent calls with the same arguments should return the cached value instantly, 
without executing the original function again. Remember to turn the kwargs mapping into a hashable form (e.g., frozenset).
"""