"""
1 ) ----- Simple logger
    Write a decorator called log_calls. Every time a function wrapped with @log_calls is invoked, 
    it should print the message Calling <function_name> before executing the original body. 
Use functools.wraps so the wrapped function retains its original name and docstring.
"""