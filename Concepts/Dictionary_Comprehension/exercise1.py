"""
## Ejercicio 1 (Revisado): Análisis de Vocabulario
Tienes una lista de palabras. Crea un diccionario que contenga solo las palabras con más de 4 letras.
    La clave debe ser la palabra en MAYÚSCULAS.
    El valor debe ser una tupla que contenga dos elementos: la longitud de la palabra y su primera letra en minúscula.
"""
def main():
    vocabulario = ["Python", "entrevista", "solucion", "reto", "es", "muy", "bueno"]
    print(
        {word.upper() : (len(word), word[0].lower()) for word in vocabulario}
    )
main()
 