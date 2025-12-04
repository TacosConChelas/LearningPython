import os

def main():
    print("--- Iniciando Contenedor Safe Divider ---")
    
    # EXPLICACIÓN TÉCNICA:
    # os.getenv('NOMBRE', 'VALOR_DEFECTO') busca una variable en el sistema.
    # Como las variables de entorno son siempre TEXTO (strings), 
    # las envolvemos en int() o float().
    try:
        a = float(os.getenv("NUM_A", 10)) # Si no encuentra NUM_A, usa 10
        b = float(os.getenv("NUM_B", 2))  # Si no encuentra NUM_B, usa 2
    except ValueError:
        print("Error: Las variables de entorno deben ser números.")
        return

    # Usamos tu lógica de generador
    divider = safe_divider()
    next(divider) # Cebado del generador
    
    resultado = divider.send((a, b))
    print(f"Dividiendo {a} / {b}")
    print(f"Resultado: {resultado}")

def safe_divider():
    result = None
    while True:
        data = yield result
        if data is None: break
        a, b = data
        try:
            result = a / b
        except ZeroDivisionError:
            result = "inf"

if __name__ == "__main__":
    main()