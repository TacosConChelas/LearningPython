def main():
    pwd = "22wdsfsfsM"
    print(validar_contraseña(pwd))


def validar_contraseña(pwd):
    lenght, lower, isSuper, isnumber = False, False, False, False
    
    if len(pwd) >= 8:
        lenght = True
    for character in pwd:
        if character.islower():
            lower = True
        elif character.isupper():
            isSuper = True
        elif(character.isdigit()):
            isnumber = True
    return lenght and lower and isSuper and isnumber
main()