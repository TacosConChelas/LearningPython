"""
## Ejercicio 3 (Revisado): Matriz de Datos Numéricos
A partir de una lista de números, crea un diccionario.
    La clave debe ser el número original.
    El valor debe ser otro diccionario que contenga dos pares clave-valor: 'cuadrado' con el valor del número al cuadrado, y 'cubo' con el valor del número al cubo.
    Incluye en el resultado final únicamente los números que sean divisibles entre 3.
"""
def main():
    numeros = [2, 3, 5, 6, 9, 10]
    print(
        {number : {"cuadrado" : number ** 2 , "cubo" : number ** 3} for number in numeros if number % 3 == 0}
    )
main()