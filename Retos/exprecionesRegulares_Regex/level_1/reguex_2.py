"""
Dado:
    texto = "Python es un Lenguaje de Programación Genial"
Encuentra todas las palabras que empiezan con mayúscula.
"""

import re


def main():
    texto = "Python es un Lenguaje de Programación Genial"
    print(re.findall(r"[A-Z]\w+", texto))

if __name__ == "__main__":
    main()    
