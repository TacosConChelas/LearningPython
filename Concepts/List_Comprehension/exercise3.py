"""
Ejercicio 3: Convertir a mayúsculas 
Tienes una lista de palabras. Crea una nueva lista con todas las palabras convertidas a mayúsculas.
"""
def main():
    palabras = ["hola", "diferente", "cybersecurity", "comercio", "python", "java", "recordatorio"]
    print([palabra.upper() for palabra in palabras])
main()