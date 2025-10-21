def main():
    pwd = "22wdsfsfs"
    print(validar_contraseña(pwd))


def validar_contraseña(pwd):
    points = 0
    mayus = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", 
        "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", 
        "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    minus = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i",
        "j", "k", "l", "m", "n", "ñ", "o", "p", "q", 
        "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if len(pwd) >= 8:
        points += 1
    for character in pwd[:]:
        if (character in mayus):
            points += 1
            break
    for character in pwd[:]:
        if (character in minus):
            points += 1
            break
    for character in pwd[:]:
        if (character in numbers):
            points += 1
            break
    return points == 4
main()