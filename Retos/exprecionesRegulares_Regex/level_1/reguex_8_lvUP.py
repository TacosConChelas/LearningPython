"""
Comprobar si una cadena contiene solo letras
Crea una función:
    def solo_letras(cadena):
    # tu regex aquí
👉 Que devuelva True si la cadena contiene solo letras (sin espacios ni números).
"""
import re


def main():
    print(solo_letras("holacomoestan"))
    print(solo_letras("hola como estan9"))
def solo_letras(cadena: str) -> bool:
    return bool(re.fullmatch(r"^[a-zA-Z]+$", cadena)) 
if __name__ == "__main__":
    main()