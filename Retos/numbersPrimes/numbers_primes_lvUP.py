from ast import List

numbers_primes = []
def main() -> None:
    try:
        number = int(input("Enter the number you want to reach the secuence of numbers primes: ").replace(" ", ""))
        print(primes_upto_(number))
    except: 
        print("Invalid number")

def primes_upto_(number: int) -> list[int]:
    if number < 2:
        return []
    return [num for num in range(2, (number + 1), 1) if is_prime(num)]

def is_prime(number: int) -> bool:
    for n in numbers_primes:
        if (number % n == 0):
            return False
    numbers_primes.append(number)        
    return True
    
if __name__ == "__main__":
    main()