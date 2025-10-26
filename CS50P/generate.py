import random


def main():
    # number = random.chose(['heads, tails'])
    # number = random.randint(1, 10)
    names = ["Jana", "Jose", "Pepe", "Pablo"]
    random.shuffle(names)
    print(names)

if __name__ == "__main__":
    main()