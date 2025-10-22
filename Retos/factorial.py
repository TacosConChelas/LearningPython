def main():
    number = int(input("Enter the number: ").strip())
    print(f"The result is: {factorial(number)}")
    
def factorial(number):
    tot = 1
    for n in range(number, 1, -1):
        # print(n)
        tot *= n
    return tot
main()