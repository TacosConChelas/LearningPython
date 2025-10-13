def main():
    lista = [10, 20, 30, 40, 50]
    print(f"La lista original es: {lista}")
    print(f"La lista invertida es: {reverse_list(lista)}")

def reverse_list(lista):
    # return lista[::-1]
    # return lista.reverse()
    lista2 = []
    up = len(lista) - 1
    for i in range(up, -1, -1):
        lista2.append(lista[i])
    return lista2


main()