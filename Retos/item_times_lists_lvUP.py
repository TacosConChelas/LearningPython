"""
Versión optimizada: O(n) en lugar de O(n²)

Crea un array nuevo el resultado de multiplicar 
cada elemento de un arreglo previo exepto el mimo elemento
"""


def product_except_self_optimized(numbers: list[int]) -> list[int]:
    """
    Calcula el producto usando prefijos y sufijos.
    Complejidad: O(n) tiempo, O(n) espacio
    """
    if not numbers:
        return []
    
    n = len(numbers)
    result = [1] * n
    
    # Productos de izquierda a derecha
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= numbers[i]
    
    # Productos de derecha a izquierda
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= numbers[i]
    
    return result


def main():
    array1 = [2, 4, 7, 6, 8, 9, 10, 3, 4, 1, 2]
    resultado = product_except_self_optimized(array1)
    
    print("Array original:", array1)
    print("Productos:", resultado)


if __name__ == "__main__":
    main()