"""
4) ------ Running average coroutine
Build a generator averager() that, after being primed with next(g), receives 
numbers via g.send(value) and yields the current arithmetic mean after each new value. 
Keep track of a running total and count inside the generator.
"""