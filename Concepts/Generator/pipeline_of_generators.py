"""
9) ----- Pipeline of generators – Construct three small generators:
    - source(iterable) yields each element of the supplied iterable.
    - filter_even(gen) yields only the even numbers coming from its upstream generator.
    - square(gen) yields the square of each incoming value.

Chain them together to compute the sum of squares of all even numbers from 1 to 1000 without creating any intermediate containers:

    total = sum(square(filter_even(source(range(1, 1001)))))

"""
