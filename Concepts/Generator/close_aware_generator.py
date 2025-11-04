"""
7)------ Close-aware generator
Create resource_user() that prints "open" when the generator is first advanced, 
then yields control indefinitely (e.g., while True: yield). When the caller 
invokes g.close(), the generator should execute a finally block that prints "closed". 
Demonstrate that closing the generator triggers the cleanup message.
"""