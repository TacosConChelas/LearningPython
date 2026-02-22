# create a greeting, create your word list, randomly choose a word from the
# list you have created, ask the user to guess a letter, make the program 
# take the input from the user and make it lowercase, check if the letter is in the word
import random
import re
def main():
    word_list = ['candy', 'boy', 'horse', 'toy', 'animal']
    print(f'Those are the word that you have to guess: {word_list}')
    guess_the_word(random.choice(word_list))
    
def guess_the_word(random_choose="") -> None:
    opptortunities = 0
    letter_matches = ""
    while opptortunities < len(random_choose):
        try:
            #print(random_choose)
            letter = str(input("Enter the letter: ").lower()).strip()
            if letter in random_choose:
                opptortunities += 1
                letter_matches += letter
                print(f"Good job! you need to guess the word in {len(random_choose) - opptortunities } attempts")
                print(re.sub(f"[^{letter_matches}]", "_", random_choose))
            else:
                print("Try again!")
        except ValueError:
            print("Enter a valid letter")
    print('You win!')
    return


if __name__ == "__main__":
    main()
