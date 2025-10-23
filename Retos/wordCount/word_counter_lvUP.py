"""
Qué significa r"[^\w\s]"

En Python (y en la mayoría de los lenguajes que usan expresiones regulares) esa cadena es una expresión regular que sirve para buscar cualquier carácter que NO sea:

    \w – word character → letras, dígitos o el guion bajo (a‑z, A‑Z, 0‑9, _).
    \s – whitespace → cualquier espacio en blanco (espacio, tabulación \t, salto de línea \n, etc.).

El ^ dentro de los corchetes ([...]) invierte el conjunto, es decir, “cualquier cosa excepto lo que está listado”.
En resumen

[^\w\s]   →   cualquier carácter que no sea letra, número, guion bajo ni espacio.

Por qué se escribe con r (raw string)

pattern = r"[^\w\s]"

    r delante de la comilla indica raw string (cadena “cruda”).
    Dentro de una raw string los \ se conservan tal cual, sin necesidad de escaparlos.

Si no usaras raw string tendrías que escribir:

pattern = "[^\\w\\s]"      # cada barra invertida se escapa con otra barra

Eso explica por qué a veces ves la forma con dobles barras (\\w, \\s). Con r es mucho más legible.

"""
import re
from typing import Counter


def main():
    phrase = str(input("Enter the phrase: ")).strip().lower()
    print(word_count(phrase))

def word_count(phrase: str) -> dict:
    phrase = re.sub(r"[^\w\s]", " ", phrase.lower()).split()
    # return {word : phrase.count(word) for word in phrase}
    return dict(Counter(phrase))

if __name__ == "__main__":
    main()