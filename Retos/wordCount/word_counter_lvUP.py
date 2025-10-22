import re
from typing import Counter


def main():
    phrase = str(input("Enter the phrase: ")).strip().lower()
    print(word_count(phrase))

def word_count(phrase: str) -> dict:
    phrase = re.sub(r"[^\w\s]", " ", phrase.lower()).split()
    # return {word : phrase.count(word) for word in phrase}
    return dict(Counter(phrase))

if __name__ == "__main__":
    main()