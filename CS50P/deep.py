def main():
    phrase = str(input("What is the Answer to the Great Question of Life, the Universe and Everything?"))
    phrase = phrase.lower().strip()

    if valid_number(phrase):
        print("Yes")
    else:
        print("No")


def valid_number(number):
    return (number == "forty-two" or number == "forty two" or number == "42")


main()
