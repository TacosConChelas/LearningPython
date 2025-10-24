"""
Encontrar todas las vocales
Dado:
    texto = "Expresiones Regulares en Python"
👉 Muestra una lista con todas las vocales (mayúsculas y minúsculas).
"""
import re


def main():
    texto = "Expresiones Regulares en Python"
    print(re.findall(r"[aeiou]", texto, flags=re.I))
if __name__ == "__main__":
    main()