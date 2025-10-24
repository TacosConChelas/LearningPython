"""
Buscar un patrón simple
Verifica si el texto comienza con la palabra "Hola":
    texto = "Hola, cómo estás?"
Usa re.match() o re.search() y devuelve True/False.
"""
import re


def main():
    texto = "Hola, cómo estás?"
    print(bool(re.match(r"Hola", texto))) 
    # Aeasy option print(texto.startswith("Hola"))

if __name__ == "__main__":
    main()