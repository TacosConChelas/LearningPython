# Dato un arreglo regresa otro arreglo que contenga el productos de todos los números exepto del número
# que estaba en esa posición

def main():
    numeros = [3, 4, 2, 5, 1]
    numeros_new = []
    for i in range(len(numeros)):
        total = 1
        # print(f"{i} )", total)

        for n in numeros:

            if numeros[i] != n:
                # print(f"tot: {total} y n {n}")      
                total = total * n
            

        numeros_new.append(total)
        # print(f"{i} )", total)

    print(numeros_new)


main()