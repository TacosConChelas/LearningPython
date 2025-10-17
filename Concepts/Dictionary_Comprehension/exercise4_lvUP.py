"""
## Ejercicio 4 (Revisado): Procesamiento de Notas de Examen
    Tienes un diccionario con nombres de estudiantes y sus calificaciones. 
    Crea un nuevo diccionario que contenga únicamente a los estudiantes aprobados (calificación mayor a 6).
    La clave debe ser el nombre del estudiante con la primera letra en mayúscula (capitalizado).
    El valor debe ser la calificación original más 5 puntos extra de bonificación.
"""
def main():
    calificaciones = {"ana": 5, "juan": 8, "carlos": 10, "sofia": 7}
    print(
        {student.capitalize() : (calificacion + 5) for student, calificacion in calificaciones.items() if calificacion > 6}
    )
main()