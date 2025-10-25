

def convert(time_str: str) -> float:
    """
    Convierte una hora escrita en formato 24 h («h:mm» o «hh:mm») a
    un número de horas tipo float.

    Ejemplos:
        "7:30"  → 7.5
        "12:05" → 12.083333...
    """
    # Separar horas y minutos
    hours_part, minutes_part = time_str.split(":")
    # Convertir a enteros
    hours = int(hours_part)
    minutes = int(minutes_part)
    # Cada 60 minutos equivale a 1 hora
    return hours + minutes / 60.0


def main() -> None:
    """
    Pide al usuario una hora y muestra, si corresponde,
    «breakfast time», «lunch time» o «dinner time».
    Si la hora no está dentro de ninguno de los intervalos,
    no se imprime nada.
    """
    # Lectura del dato del usuario (se asume formato correcto)
    time_input = input("What time is it?").strip()

    # Convertimos a número de horas
    hour_float = convert(time_input)

    # print(hour_float)


    # Rango de desayunos: 7:00 – 8:00 (inclusive)
    if 7.0 <= hour_float <= 8.0:
        print("breakfast time")
    # Rango de almuerzos: 12:00 – 13:00 (inclusive)
    elif 12.0 <= hour_float <= 13.0:
        print("lunch time")
    # Rango de cenas: 18:00 – 19:00 (inclusive)
    elif 18.0 <= hour_float <= 19.0:
        print("dinner time")
    # Si no está en ningún rango, no hacemos nada (no imprimimos nada).


if __name__ == "__main__":
    main()
