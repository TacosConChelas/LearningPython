def main():
    
    print(f"Resultado frase 1: {es_palindromo("Anita lava la tina")}")

    print(f"Resultado frase 2: {es_palindromo("Reconocer")}")

    print(f"Resultado frase 3: {es_palindromo("Hola Mundo")}")
    ## print(phrase2[::-1])


def es_palindromo(phrase):
    
    phrase = str(phrase).lower().replace(" ", "")

    # YA NO SE USA phrase = "".join(phrase.split()) NI .split()
    # phrase = phrase.replace(" ", "")
    return phrase == phrase[::-1]

main()