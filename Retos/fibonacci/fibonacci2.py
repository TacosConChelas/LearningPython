def main():
    try:
        number = int(input("Enter the number: ").strip())
        print(fibonacci_to(number))
    except:
        print("Enter a valid number")

def fibonacci_to(number):
    a, b = 0, 1
    numbers =[]
    for _ in range(number):
        a, b = b, (b + a)
        numbers.append(a) 
    return numbers
main()