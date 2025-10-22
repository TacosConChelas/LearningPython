def main() -> None:
    while True:
        number = str(input("Enter the number: ")).replace(" ", "")
        if number.isdigit():
            print(is_palindrome_(number))
            break
        print("Enter a correct number")

def is_palindrome_(number:str) -> str:
    return "Es palindromo" if number == number[::-1] else "No es palindromo" 

if __name__ == "__main__":
    main()