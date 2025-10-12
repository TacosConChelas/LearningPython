def main():
    resultado = analizar_texto("Hola mundo 123")
    print(resultado)

   

def analizar_texto(texto):
    texto = texto.lower()

    consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    vocales = ["a", "e", "i", "o", "u"]

    # resultado = {letter : consonantes.count(letter) for _ in consonantes}
    #resultado = {letter = }    
    tot_c = 0
    tot_v = 0
    for i in range(len(texto)):
        tot_c += consonantes.count(texto[i])
        tot_v += vocales.count(texto[i])
    return {"vocales" : tot_v, "consonantes" : tot_c}

main()