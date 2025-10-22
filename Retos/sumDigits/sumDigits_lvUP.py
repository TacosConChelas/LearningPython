def main():
    while True:
        number = input("Enter a positive number: ").strip()
        try:
            if number.isdigit():
                print(sum_digits(number))
                break
            print("Invalid number")
        except ValueError:
            print("Invalid number entered")        

def sum_digits(number: str) -> int:
    return sum(int(num) for num in number)

if __name__ == "__main__":
    main()