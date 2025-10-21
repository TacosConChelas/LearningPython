def main():
    phrase = str(input("Enter the phrase: ")).strip()
    print(word_count(phrase))
def word_count(phrase):
    phrase = phrase.split(" ")
    return {word : phrase.count(word) for word in phrase}
main()