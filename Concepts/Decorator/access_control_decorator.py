"""
5) ------ Access‑control decorator 
Write a decorator factory requires_role(role) that checks a global variable CURRENT_USER_ROLE. 
If the current role does not match the required one, raise PermissionError; otherwise call the 
wrapped function. Use the outer function to capture the required role and the inner wrapper to 
perform the check.
"""
