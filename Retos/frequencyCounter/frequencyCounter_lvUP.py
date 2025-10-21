def main():
    elementos1 = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4, 7, 7, 8, 4, 3, 7, 9, 0, 0, 7, 5]
    elementos2 = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]
    print(contador_de_frecuencia(elementos1))
    print(contador_de_frecuencia(elementos2))

def contador_de_frecuencia(elementos):    
    elementos_contados = {}
    # print("_1")
    
    for elemento in elementos:
        # print("_2")
        # if not (elemento in elementos_contados.keys()): 
        if elemento in elementos_contados:
            #elementos_contados.update({elemento : elementos.count(elemento)})
            elementos_contados[elemento] += 1
        else:
            elementos_contados[elemento] = 1
        
    return elementos_contados

main()