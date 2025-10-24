"""
    Problem:
        texto = "Python es un Lenguaje de Programación Genial"
    Encuentra todas las palabras que empiezan con mayúscula.

    if you'll reuse the pattern or if the file is gonna process a lot of text, you can compile 
        pattern = re.compile(r"\b[A-Z][a-Záéíóúüñ]")             
    and use
        pattern.findall(text)
"""
import re

def main():
    texto = "Python es un Lenguaje de Programación Genial"
    print(re.findall(r"\b[A-Z][a-Záéíóúüñ]", texto))

if __name__ == "__main__":
    main()    
