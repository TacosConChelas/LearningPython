def main():
    compras = [
        ("Manzana", 2.50, 4),   # 2.50 * 4 = 10.00
        ("Leche", 22.00, 1),   # 22.00 * 1 = 22.00
        ("Pan", 5.00, 2)       # 5.00 * 2 = 10.00
    ]
    print(f"El costo total es: ${total_calcular(compras)}")

def total_calcular(compras):
    total = 0
    for compra in compras:
        total = float(total + (compra[1] * compra[2]))
    return total

main()ajajajja