def main():
    phrase = str(input("camelCase: "))
    turn_to_snake(phrase)
    # if phrase.isupper(): print("mayus")
    # print("Hola".replace("", " ").strip().split(" "))

def turn_to_snake(phrase):
    phrase = phrase.replace("", " ").strip().split(" ")
    rango = len(phrase)
    i = 0

    while i < rango:
        if phrase[i].isupper():
            # print("_")
            # phrase[i].lower()
            phrase.insert(i, "_")
            rango += 1
            i += 1
        i += 1
    print(f"snake_case: {("".join(phrase)).lower()}")


main()