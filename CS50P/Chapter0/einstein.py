
def main():
    phrase = input("m: ")
    phrase = phrase.split()

    m = float(phrase[-1])

    print(f"E: {einstein(m):.0f}")

def einstein(m=0):
    c = 300000000

    return float(m * (c ** 2))


main()