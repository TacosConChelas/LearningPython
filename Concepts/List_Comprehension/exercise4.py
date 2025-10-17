"""
Ejercicio 4: Extraer el primer carácter 
Dada una lista de frutas, crea una nueva lista que contenga solo la primera letra de cada fruta, 
pero únicamente de aquellas frutas que tengan más de 5 letras.
"""
def main():
    frutas = ["manzana", "pera", "uva", "naranja", "sandia", "kiwi"]
    print([fruta[0] for fruta in frutas if len(fruta) > 5])
main()