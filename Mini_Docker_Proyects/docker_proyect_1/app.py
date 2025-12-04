# app.py
import time
import os

def countdown(n):
    while n > 0:
        yield n
        n -= 1

def main():
    # reading a evironment variable 
    # if it doesn't exist, by default it starting in 5
    start_num = int(os.getenv("START_NUMBER", 5))
    
    print(f"--- Iniciando conteo desde {start_num} en un contenedor ---")
    
    gen = countdown(start_num)
    
    for num in gen:
        print(f"Conteo: {num}")
        time.sleep(1) # Simula un proceso trabajando
    
    print("--- ¡Proceso finalizado! ---")

if __name__ == "__main__":
    main()