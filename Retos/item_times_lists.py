"""
Crea un array nuevo el resultado de multiplicar 
cada elemento de un arreglo previo exepto el mimo elemento
"""
def main():
    array1 = [2, 4, 7, 6, 8, 9, 10, 3, 4, 1, 2]
    # function_lamda = lambda x, y: x * y if x != y else 1
    array2 = [f"{total_(number, array1)}" for number in array1]
    print(" ".join(array2))
def total_(number, numbers : list):
    total = number
    for item in numbers:
        if number != item:
            total *= item 
    return total
    

if __name__ == "__main__": 
    main()
