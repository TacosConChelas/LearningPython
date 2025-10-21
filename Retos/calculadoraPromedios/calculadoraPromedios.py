calificaciones_estudiantes = {
        "Ana" : [90, 85, 95],
        "Luis" : [78, 88, 90],
        "Fernando" : [65, 99, 87],
        "Angel" : [88, 79, 64]
}
def main():
    print(calcular_promedio("Ana"))    

def calcular_promedio(estudiante):
    for key, values in calificaciones_estudiantes.items():
        if key == estudiante:
            tot = 0
            for value in values:
                tot += value
             
            tot = float(tot / len(values)) 
    #if tot == 0:
    #    calificaciones_estudiantes.keys
    if estudiante in calificaciones_estudiantes.keys():
        return f"El estduiante {estudiante} con promedio de {tot}"
    else: 
        return "No se ha encontrado al estudiante"


main()