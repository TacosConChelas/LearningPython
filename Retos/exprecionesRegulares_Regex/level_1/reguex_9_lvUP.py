"""
Extraer los números de teléfono
Dado
    texto = "Contactos: 123-456-789, 987-654-321"
👉 Extrae todos los teléfonos del formato xxx-xxx-xxx.
"""
import re


def main():
    texto = "Contactos: 123-456-789, 987-654-321"
    print(re.findall(fr"\d{3}-\d{3}-\d{3}", texto)) 

if __name__ == "__main__":
    main()