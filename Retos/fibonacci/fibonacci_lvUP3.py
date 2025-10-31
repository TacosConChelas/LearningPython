def main():
    try:
        number = int(input("Escribe le tamaño dela secuencia de Fibonacci que quieres que se haga: "))
        print(generar_fibonacci(number))
    except ValueError:
        print("Enter a valid value")
def generar_fibonacci(n : int) -> list[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fibonacci = [0, 1]
    for _ in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

if __name__ == "__main__":
    main()