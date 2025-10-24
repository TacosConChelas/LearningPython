"""
Encontrar dominios web
Dado:
    texto = "Visita openai.com y python.org para aprender más."
👉 Extrae los nombres de dominio (openai.com, python.org).
"""
import re


def main():
    texto = "Visita openai.com y python.org para aprender más."
    patron = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'
    print(re.findall(patron, texto))

if __name__ == "__main__":
    main() 