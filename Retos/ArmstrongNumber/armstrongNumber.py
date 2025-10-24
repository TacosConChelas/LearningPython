def main():
    try:
        number = input("Enter the number: ").replace(" ", "")
        print(is_armstrong(number))
    except ValueError:
        print("Enter a valid number")
def is_armstrong(number : str) -> bool:
    k_number = len(number)
    numbers = sum(int(n) for n in number)
    return numbers == int(number)
main()