# create a greeting, create your word list, randomly choose a word from the
# list you have created, ask the user to guess a letter, make the program 
# take the input from the user and make it lowercase, check if the letter is in the word
import random
import re
def main():
    word_list = ['candy', 'boy', 'horse', 'toy']
    print(f'Those are the word that you have to guess: {word_list}')
    guess_the_word(random.choice(word_list))
    
def guess_the_word(random_choose="") -> None:
    opptortunities = 0
    letter_matches = ""
    while opptortunities < 5:
        try:
            print(random_choose)
            letter = str(input("Your secret word is like this: " + "_"*len(random_choose) + f"\nEnter the letter, (you only have 5 guesses): ").lower()).strip()
            if letter in random_choose:
                letter_matches += letter
                new_word = re.sub(f"[^{letter_matches}]", "_", random_choose)
                if new_word == random_choose:
                    print('You win'); return
                print('Good job!', new_word)
            else:
                print("Try again!")
        except ValueError:
            print("Enter a valid letter")
        opptortunities += 1

if __name__ == "__main__":
    main()
