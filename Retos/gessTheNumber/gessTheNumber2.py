import random


def main() -> None:                                                                      
    random_number = random.randint(1, 100)
    intentos = 0
    while True:
        try:
            number = int(input(f"Intentos: {intentos} \nTry to gess the random number: ").strip())
            # print(random_number)
            if number > random_number:
                print("Less!")
            elif number < random_number:
                print("More!")
            else:
                print("You win! Good Game!")
                break
            intentos += 1
        except ValueError:
            print("Enter a valid number")
        except EOFError:
            break
if __name__ == "__main__":
    main()