"""
6) ------- Retry decorator
Implement retry(attempts=3, delay=0.5). The wrapper should call the target function, 
and if it raises any exception, wait delay seconds and retry, up to attempts times. 
If the final attempt still fails, re-raise the exception. This exercise introduces time.sleep, 
a try/except loop, and the need to preserve the original function's signature.
"""
