"""
Ejercicio 2: Números impares a partir de un rango 
Crea una lista que contenga todos los números impares del 1 al 20.
"""
def main():
    print([number for number in range(1, 20) if not number % 2 == 0])
main()
