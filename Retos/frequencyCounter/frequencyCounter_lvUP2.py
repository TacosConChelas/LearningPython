def main():
    elementos1 = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4, 7, 7, 8, 4, 3, 7, 9, 0, 0, 7, 5]
    elementos2 = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]
    print(contador_de_frecuencia(elementos1))
    print(contador_de_frecuencia(elementos2))

def contador_de_frecuencia(elementos):    
    elementos_contados = {}
    
    for elemento in elementos:
        # 1) if not (elemento in elementos_contados.keys()): 
            # 1) elementos_contados.update({elemento : elementos.count(elemento)})
        # 2) if elemento in elementos_contados:
            # 2) elementos_contados[elemento] += 1
        # 2) else:
            # 2) elementos_contados[elemento] = 1

        elementos_contados[elemento] = elementos_contados.get(elemento, 0) + 1
        # Obtén el conteo actual de 'elemento' (o 0 si no existe) y súmale 1.
    return elementos_contados

main()