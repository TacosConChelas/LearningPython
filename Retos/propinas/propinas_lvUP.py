def main():
    try:
        total = float(input("Enter the total: ").strip())
        percent = float(input("Enter the percent: ").strip())
        print(tip(total, percent))
    except ValueError:
        print("Entrada no valida")

def tip(total: float, percent: float) -> float:
    if total < 0:
        print("El total no puede ser negativo")
        return
    if percent < 0:
        print("El porcentaje no puede ser negativo")
        return
    return round((total * percent) / 100, 2)

if __name__ == "__main__":
    main()