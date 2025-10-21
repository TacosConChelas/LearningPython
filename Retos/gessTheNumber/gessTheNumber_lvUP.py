import random

def main():
    number_random = random.randint(1, 100)
    while True:
        try:
            number = int(input("Adivina el numero entre 1 y 100: ").strip())

            if number > number_random :
                print("¡Muy alto!")
            elif number < number_random :
                print("¡Muy bajo!")
            else:
                break    

        except ValueError:
            print("Error eso no es un numero")            
          
    print("¡Has adivinado, muy buen juego!")            

main()