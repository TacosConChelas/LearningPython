"""
9) ------ Signature preservation
Write preserve_sig that copies the original function's signature onto the wrapper so that 
tools like help() display the correct parameter list instead of the generic *args, **kwargs. 
In Python 3.11+ you can use functools.update_wrapper with the signature= argument; for earlier 
versions you may need the third-party decorator library or inspect.signature.
"""
