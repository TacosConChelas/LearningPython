"""
5) ------ Safe divider with exception handling
Write safe_divider() that repeatedly expects a tuple (a, b) sent to it. 
It should yield a / b when b is non‑zero, but if a ZeroDivisionError occurs 
it catches the exception and yields the string "inf" instead of propagating the error.
"""
def main():
    safe = safe_divider()
    next(safe) # Cebado
    
    # Pruebas
    print(f"Enviando (2, 0): {safe.send((2, 0))}")
    print(f"Enviando (10, 2): {safe.send((10, 2))}")
    print(f"Enviando (9, 3): {safe.send((9, 3))}")

def safe_divider():
    result = None
    while True:
        # Recibimos los datos
        data = yield result
        
        # Salida de seguridad
        if data is None: 
            break
            
        # Desempaquetado (Unpacking) - Mucho más limpio que data[0]
        a, b = data
        
        try:
            # Intentamos dividir sin miedo
            result = a / b
        except ZeroDivisionError:
            # Solo entramos aquí si algo salió mal
            result = "inf"
        except TypeError:
            # Captura extra por si envían strings o datos incorrectos
            result = "error: inputs must be numbers"

if __name__ == "__main__":
    main()