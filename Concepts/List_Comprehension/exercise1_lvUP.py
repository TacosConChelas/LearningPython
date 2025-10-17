"""
Ejercicio 1: Filtrar nombres 
Tienes una lista de nombres. 
Crea una nueva lista que contenga únicamente los nombres que empiezan con la letra "A".
"""
def main():
    nombres = ["Ana", "Carlos", "Alberto", "Brenda", "Andrea"]
    # Método 1
    # new_list = [name for name in nombres if name[0] in "aAáÁ"]
    # print(new_list)
    # Método 2
    # print([name for name in nombres if name[0] in "aAáÁ"])
    # método  3
    print([name for name in nombres if name.lower().startswith('a')])
main()
