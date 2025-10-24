"""
Separar una cadena por comas o puntos y coma
Dado:
    texto = "uno, dos; tres, cuatro"
👉 Divide el texto en una lista de palabras.
"""
import re


def main():
    texto = "uno, dos; tres, cuatro"
    print(re.split(r"[.,;:]\s", texto))
if __name__ == "__main__":
    main()