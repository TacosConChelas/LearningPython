import random


def main():                                                                      
    random_number = random.randint(1, 100)
    while True:
        try:
            number = int(input("Try to gess the random number: ").strip())
            # print(random_number)
            if number > random_number:
                print("Less!")
            elif number < random_number:
                print("More!")
            else:
                print("You win! Good Game!")
                break
        except:
            print("Enter a valid number")
main()