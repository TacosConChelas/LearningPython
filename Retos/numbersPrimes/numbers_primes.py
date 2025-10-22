numbers_primes = []
def main():
    try:
        number = int(input("Enter the number you want to reach the secuence of numbers primes: ").strip())
        print(primes_upto_(number))
    except: 
        print("Invalid number")
def primes_upto_(number):
    return [num for num in range(1, (number + 1), 1) if is_prime(num)]
def is_prime(number):
    for n in numbers_primes:
        if (number % n == 0) and n != 1:
            return False
    numbers_primes.append(number)        
    return True
main()