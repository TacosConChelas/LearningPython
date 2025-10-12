def main():
    phrase = str(input("Enter your phrase: "))

    phrase_new = volvear(phrase)

    if (phrase == phrase_new):
        print("Es un palindromo!")
    else:
        print("No es un palindromo!")


def volvear(phrase):
    phrase_new = ""
    c = len(phrase) - 1
    while c >= 0:
        phrase_new += phrase[c]
        c -= 1

    return phrase_new

main()