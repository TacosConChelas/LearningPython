WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")
  

    for word, points in WORDS.items():
        print(f"{word} was worth {points} ")

    print("that's the game!")



main()