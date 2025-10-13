calificaciones_estudiantes = {
        "Ana" : [90, 85, 95],
        "Luis" : [78, 88, 90],
        "Fernando" : [65, 99, 87],
        "Angel" : [88, 79, 64]
}
def main():
    print(calcular_promedio("Ana"))    

def calcular_promedio(estudiante):
    if not (estudiante in calificaciones_estudiantes.keys()):
        return "No se ha encontrado al estudiante"
    else:
        values = calificaciones_estudiantes[estudiante]    
        tot = float(sum(values) / len(values))
        return f"El estduiante {estudiante} con promedio de {tot}"
    
main()