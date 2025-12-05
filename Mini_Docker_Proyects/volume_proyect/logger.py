# logger.py
import time
from datetime import datetime

def main():
    print("--- Iniciando Logger ---")
    # Abrimos en modo 'a' (append) para no borrar lo anterior
    with open("bitacora.txt", "a") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[LOG] Evento registrado a las {now}\n"
        f.write(log_entry)
        print(f"Escribiendo: {log_entry.strip()}")
    
    print("--- Fin del proceso ---")

if __name__ == "__main__":
    main()