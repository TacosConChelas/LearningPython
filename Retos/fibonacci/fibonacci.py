def main():
    number = int(input("Escribe le tamaño dela secuencia de Fibonacci que quieres que se haga: "))
    if number > 0: 
        print(generar_fibonacci(number))
    else:
        print("Elija un numero valido")

def generar_fibonacci(n):
    fibonacci = [0, 1]
    match(n):
        case 2:
            return fibonacci
        case 1:
            return [0]
        case _:
            for i in range(n - 2):
                fibonacci.append(fibonacci[i] + fibonacci[i + 1])
            return fibonacci
main()