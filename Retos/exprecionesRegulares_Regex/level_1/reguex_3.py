"""
Extraer todas las palabras
De este texto:
    texto = "Hola mundo, hoy es 22 de Octubre!"
👉 Usa regex para obtener todas las palabras (sin signos).
"""
import re


def main():
    texto = "Hola mundo, hoy es 22 de Octubre!"
    print(re.findall(r"\w+", texto))

if __name__ == "__main__":
    main()