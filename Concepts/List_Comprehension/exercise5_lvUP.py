"""
Ejercicio 5: Precios con IVA Tienes una lista de precios sin IVA. 
Crea una nueva lista con los precios finales después de agregarles el 16% de IVA (es decir, multiplicando por 1.16), 
pero solo para los precios que sean mayores a 20.
"""
def main():
    precios_sin_iva = [15.50, 25.00, 10.00, 50.75, 18.20]
    print([round(precio * 1.16, 2) for precio in precios_sin_iva if precio > 20])
main()