

def main():
    x = int(input("Enter the value of X: "))

    if is_even(x):
        print("Event")
    else:
        print("Odd")

def is_even(n):
    return (n % 2 == 0)

main()


