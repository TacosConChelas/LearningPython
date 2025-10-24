"""
Dado::
texto = "Usuario123 con clave456"
Reemplaza todos los números por #.
"""
import re


def main():
    texto = "Usuario123 con clave456"
    print(re.sub(r"\d", "#", texto))
if __name__ == "__main__":
    main()