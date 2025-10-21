def main():
    agenda = {
        "Jose" : 7831386638,
        "Fernando" : 7831386639,
        "Angel" : 7831386640,
        "Juan" : 7831386641,
        "Pedro" : 7831386642,
        "Maria" : 7831386643,
        "Ana" : 7831386644,
        "Luis" : 7831386645,
        "Carlos" : 7831386646,
        "Miguel" : 7831386647
    }

    buscar = str(input("Ingresa el contacto que deceas buscar: "))

    if not (buscar_contacto(agenda, buscar) == None):
        contacto = buscar_contacto(agenda, buscar)
        print(f"El contacto {contacto[0]} tiene el numero {contacto[1]}")

def buscar_contacto(agenda, nombre):
    if nombre in agenda.keys():
        return (nombre, agenda[nombre])
    else:
       return None

main()