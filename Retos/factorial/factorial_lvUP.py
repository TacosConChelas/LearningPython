def main():
    while True:
        try:
            number = int(input("Enter the number: ").strip())
            print(f"The result is: {factorial(number)}")
            break
        except ValueError:
            print("Enter a valid number") 
def factorial(number):
    if number <= 0:
        return 0
    tot = 1
    for n in range(2, number + 1):
        tot *= n
    return tot
if __name__ == "__name__":
    main()