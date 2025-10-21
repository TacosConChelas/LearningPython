def main():
    try:
        number = str(input("Enter the number: ")).replace(" ", "")
        print(is_palindrome_number(number))
    except:
        print("Enter a correct number")
def is_palindrome_number(number):
    return "Es palindromo" if number == number[::-1] else "No es palindromo" 
main()