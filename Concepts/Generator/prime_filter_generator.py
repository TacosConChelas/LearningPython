"""
2) ----- Prime filter generator
Implement primes(limit) that yields every prime number less than or equal to limit. 
Use a helper is_prime inside the generator and yield each prime you discover.
"""
def main():
    print(list(primes(4)))
def primes(limit : int):
    if limit < 2: 
        return None
    if limit == 2:
        yield 2
    prime_nums = [2]
    for i in range(2, limit):
        if is_another_prime(i, prime_nums):
            prime_nums.append(i);
            yield i            
def is_another_prime(number : int, numbers : list[int]) -> bool:
    for n in numbers:
        if number % n == 0:
            return False
    return True
if __name__ == "__main__":
    main()