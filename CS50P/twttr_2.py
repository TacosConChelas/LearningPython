def main():
    phrase = str(input("Input: "))

    pop_vocals(phrase)

def pop_vocals(phrase):
    vocals = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    phrase = phrase.strip()
    for p in phrase:
        if p in vocals:
            phrase = phrase.replace(p, "")

    print(f"Output: {phrase}")
main()