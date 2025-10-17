"""
## Ejercicio 5 (Revisado): Limpieza y Conversión de Datos
    Tienes un diccionario de productos con precios guardados como strings que incluyen el símbolo de moneda. 
    Crea un diccionario limpio que solo contenga los productos cuyo precio sea menor a 100.00.
    La clave debe ser el nombre del producto (el mismo).
    El valor debe ser el precio convertido a un número de punto flotante (float).
"""
def main():
    precios_str = {"monitor": "$199.99", "mouse": "$24.50", "usb-c cable": "$12.00", "webcam": "$85.75"}
    print(
        {product.capitalize() : float(precios_str[product][1:]) for product in precios_str.keys() if float(precios_str[product][1:]) < 100}
    )
main()