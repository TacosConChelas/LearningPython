def main():
    try:
        number = int(input("Enter the number: ").strip())
        print(fibonacci_to(number))
    except ValueError:
        print("Enter a valid number")

def fibonacci_to(number : int) -> list[int]:
    if number <= 0:
        return []
    a, b = 0, 1
    numbers =[]
    for _ in range(number):
        a, b = b, (b + a)
        numbers.append(a) 
    return numbers
if __name__ == "__main__":
    main()