def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # print(f"{valid_letters(s)} and {valid_lenght(s)} and {valid_numbers(s)} and {invalid_characters(s)}")
    return valid_letters(s) and valid_lenght(s) and valid_numbers(s) and invalid_characters(s)
#1            
def valid_letters(s):
    letters = "aeiouAEIUOUbcdfghjklmnñpkrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    count = 0
    for character in s:
        if count == 2:
            return True
        if character in letters:
            count += 1
    return False
#2
def valid_lenght(s):
    return 7 >= len(s) > 1
#3
def valid_numbers(s):
    numbers = "1234567890"
    middle = int(len(s) / 2)
    #1
    for i in range(middle):
        if s[i] in numbers:
            return False
    #2
    number1 = ""
    firstime = True
    for character in s:
        if character in numbers:
            if firstime:
                number1 = character
                firstime = False
    if number1 == "0":
        return False
    return True
#4
def invalid_characters(s):
    invalid_characters = "áéíóúÁÉÍÓÚ.,:; _-?¡¿!<>"
    for character in s:
        if character in invalid_characters:
            return False
    return True
    
main()
