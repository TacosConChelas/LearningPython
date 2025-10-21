def main():
    number = int(input("Escribe le tamaño dela secuencia de Fibonacci que quieres que se haga: "))
    print(generar_fibonacci(number))

def generar_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fibonacci = [0, 1]
    for _ in range(n - 2):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return fibonacci

main()