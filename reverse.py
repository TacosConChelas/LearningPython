def main():
    phrase = str(input("Enter some phrase: "))
    
    reverse1(phrase)
    

def reverse1(phrase):
    phrase_reverse = ""

    c = len(phrase) - 1
    while c >= 0 :
        phrase_reverse += phrase[c]
        c -= 1

    print(phrase_reverse)
    
# def revese2(phrase):


main()