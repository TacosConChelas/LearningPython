"""
Encontrar dominios web
Dado:
    texto = "Visita openai.com y python.org para aprender más."
👉 Extrae los nombres de dominio (openai.com, python.org).
"""
import re


def main():
    texto = "Visita openai.com y python.org para aprender más."
    print(re.findall(r'\b(?:[a-z0-9-]+\.)+[a-z]{2,}\b', texto, re.I))

    # if we want accept URLs with "https://" and/or "www." you can use this pattern:
    #   r'\b(?:https?://)?(?:www\.)?(?:[a-z0-9-]+\.)+[a-z]{2,}\b'

if __name__ == "__main__":
    main() 