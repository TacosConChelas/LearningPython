"""
    Dado el texto:
        texto = "Tengo 2 perros y 3 gatos."
    Extrae todos los números usando regex.

    if you'll reuse the pattern or if the file is gonna process a lot of text, you can compile 
    pattern = re.compile(r"\d+")             
    and use
    pattern.findall(text)
"""
import re



def main():
    texto = "Tengo 2 perros y 3 gatos."
    numbers = list(map(int, re.findall(r"\d+", texto)))
    # if you want only strings: re.findall(r"\d+", texto)
            
    print(numbers)

if __name__ == "__main__":
    main()