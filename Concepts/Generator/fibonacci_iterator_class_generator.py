"""
10) ----- Fibonacci iterator class delegating to a generator
Implement a class FibonacciIterator(n) that conforms to the iterator 
protocol (__iter__ returns self, __next__ returns the next Fibonacci number). 
Inside the class, define a private generator method _fib_gen() that yields the sequence indefinitely. 
In __init__, instantiate the generator (self._gen = self._fib_gen()) and in __next__ simply return next(self._gen). 
The iterator should stop after producing n values, raising StopIteration thereafter. Verify 
that list(FibonacciIterator(5)) yields [0, 1, 1, 2, 3].
"""