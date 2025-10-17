"""
## Ejercicio 5 (Revisado): Limpieza y Conversión de Datos
    Tienes un diccionario de productos con precios guardados como strings que incluyen el símbolo de moneda. 
    Crea un diccionario limpio que solo contenga los productos cuyo precio sea menor a 100.00.
    La clave debe ser el nombre del producto (el mismo).
    El valor debe ser el precio convertido a un número de punto flotante (float).

    una característica de Python 3.8+ llamada "walrus operator" (:=). 
    Este operador te permite asignar un valor a una variable dentro de una expresión.
    EN ESTE CASO SE CREA LA VARIBLE DENTRO DE LA CONDICION YA QUE ESTA SE RESUELVE PRIMERO y luego el clave-valor
"""
def main():
    precios_str = {"monitor": "$199.99", "mouse": "$24.50", "usb-c cable": "$12.00", "webcam": "$85.75"}
    print(
        {product.capitalize() : price_float for product, price in precios_str.items() if (price_float := float(price[1:])) < 100}
    )
main()