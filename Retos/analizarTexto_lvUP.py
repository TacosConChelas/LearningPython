def main():
    resultado = analizar_texto("Hola mundo 123")
    print(resultado)

def analizar_texto(texto):
    texto = texto.lower()

    consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    vocales = ["a", "e", "i", "o", "u"]
  
    tot_c = 0
    tot_v = 0
    for character in texto:
        if character in consonantes: tot_c += 1
        elif character in vocales: tot_v += 1
    return {"vocales" : tot_v, "consonantes" : tot_c}

main()