"""
6) ----- Lazy file line reader
Implement read_lines(path) that opens a text file and yields one line at a time, 
stripped of its trailing newline character. The function must use a with open(...) 
as f: block and a simple for line in f: loop, ensuring that the file is never fully loaded into memory.
"""
import os

def main():
    # 1. PREPARACIÓN: Vamos a crear un archivo de prueba para el ejercicio
    nombre_archivo = "prueba_gigante.txt"
    with open(nombre_archivo, "w") as f:
        f.write("Línea 1: Hola mundo\n")
        f.write("Línea 2: Python es eficiente\n")
        f.write("Línea 3: Los generadores ahorran RAM\n")
        f.write("Línea 4: Fin del archivo")

    print(f"--- Leyendo {nombre_archivo} de forma eficiente ---")
    # 2. USO DEL GENERADOR 
    # aquí no obtenemos una lista, sino el objeto generador
    lector = read_lines(nombre_archivo)
    
    # Consumimos el generador línea por línea
    for linea in lector:
        print(f"Procesando: {linea}")
    # Limpieza (borramos el archivo de prueba)
    os.remove(nombre_archivo)
def read_lines(path):
    """
    Abre un archivo y entrega (yield) una línea a la vez.
    Nunca carga el archivo completo en memoria.
    """
    # 'r' significa modo lectura (read)
    # 'with' es un 'Context Manager': asegura que el archivo se cierre al terminar
    # aunque ocurra un error entre medio.
    with open(path, 'r') as f:
        # En Python, el objeto archivo 'f' YA ES un iterador.
        # Al hacer un bucle sobre él, Python lee inteligentemente línea por línea.
        for line in f:
            # .strip() elimina espacios en blanco y el salto de línea (\n) del final
            yield line.strip()

if __name__ == "__main__":
    main()


    