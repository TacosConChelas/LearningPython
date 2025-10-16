def main():
    phrase = str(input("Input: "))

    pop_vocals(phrase)

def pop_vocals(phrase):
    vocals = ["a", "e", "i", "o", "u"]
    phrase = phrase.strip()
    for vocal in vocals:
        phrase = phrase.replace(vocal, "")

    print(f"Output: {phrase}")
main()