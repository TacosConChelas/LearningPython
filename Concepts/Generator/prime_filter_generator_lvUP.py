"""
2) ----- Prime filter generator
Implement primes(limit) that yields every prime number less than or equal to limit. 
Use a helper is_prime inside the generator and yield each prime you discover.
"""
import math

def main():
    # Probemos con un número un poco más interesante
    print(list(primes(20)))

def primes(limit: int):
    """
    Genera números primos hasta 'limit' (inclusive) usando 
    bajo consumo de memoria.
    """
    if limit >= 2:
        yield 2  # El único primo par, lo entregamos manual
    
    # OPTIMIZACIÓN 1: Saltamos de 2 en 2 (3, 5, 7...)
    # No tiene sentido revisar números pares mayores a 2.
    for n in range(3, limit + 1, 2):
        if is_prime_optimized(n):
            yield n

def is_prime_optimized(number: int) -> bool:
    # OPTIMIZACIÓN 2: Raíz cuadrada.
    # Si un número no es divisible por nada hasta su raíz cuadrada,
    # entonces es primo.
    if number < 2: return False
    
    # isqrt es "Integer Square Root" (muy eficiente)
    sqrt_limit = math.isqrt(number)
    
    # Verificamos divisores desde 3 hasta la raíz, saltando pares
    for i in range(3, sqrt_limit + 1, 2):
        if number % i == 0:
            return False
            
    return True

if __name__ == "__main__":
    main()