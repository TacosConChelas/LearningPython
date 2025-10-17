"""
## Ejercicio 2 (Revisado): Clasificación de Inventario
Tienes un diccionario que mapea un ID de producto a su cantidad en stock. Crea un nuevo diccionario que clasifique cada producto.
    La clave debe ser el ID del producto (el mismo que el original).
    El valor debe ser la palabra "DISPONIBLE" si el stock es mayor a 0, y "AGOTADO" si el stock es 0.
"""
def main():
    inventario = {"PROD-001": 15, "PROD-002": 0, "PROD-003": 34, "PROD-004": 0}
    # inventario.get(clave)
    print(
        {clave : ("DISPONIBLE" if inventario[clave] > 0 else "AGOTADO") for clave in inventario.keys()}
    )
main()