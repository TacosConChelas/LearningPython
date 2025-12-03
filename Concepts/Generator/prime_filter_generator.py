"""
2) ----- Prime filter generator
Implement primes(limit) that yields every prime number less than or equal to limit. 
Use a helper is_prime inside the generator and yield each prime you discover.
"""
def main():
    print(list(primes(3)))
def primes(limit : int):
    if limit < 2: 
        return None
    if limit == 2:
        # the list has one number
        yield 2
    # the firt prime number is 2
    prime_nums = []
    for i in range(2, limit + 1):
        if is_another_prime(i, prime_nums):
            prime_nums.append(i)
            yield i            
def is_another_prime(number : int, numbers : list[int]) -> bool:
    for n in numbers:
        if number % n == 0:
            # isn't a prime number or is a prime number already list inside 
            return False
    # is another prime number
    return True
if __name__ == "__main__":
    main()