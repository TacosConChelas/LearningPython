import random

cards = ["Jack", "Queen", "King"]
def main():
    # random.seed(1)
    print(random.choices(cards, weights=[75, 20, 5], k=2))

main()