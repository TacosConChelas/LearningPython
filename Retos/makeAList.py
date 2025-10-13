def main():
    lista = [10, 20, 30, 40, 50]
    print(f"La lista original es: {lista}")
    print(f"La lista invertida es: {reverse_list(lista)}")

def reverse_list(lista):
    # return lista[::-1]
    # return lista.reverse()
    up = len(lista) - 1
    for i in range(up, -1, -1):
        print(lista[i])
    return lista


main()