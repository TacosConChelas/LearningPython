"""
Dado el texto:
    texto = "Tengo 2 perros y 3 gatos."
Extrae todos los números usando regex.
"""
import re


def main():
    texto = "Tengo 2 perros y 3 gatos."
    print(re.findall(r"\d+", texto))

if __name__ == "__main__":
    main()