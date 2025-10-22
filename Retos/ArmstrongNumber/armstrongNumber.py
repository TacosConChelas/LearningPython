def main():
    try:
        number = input("Enter the number: ").replace(" ", "")
        print(is_armstrong(number))
    except:
        print("Enter a valid number")
def is_armstrong(number):
    k_number = len(number)
    numbers = [int(n) for n in number]
    tot = 0
    for n in numbers:
        tot += n ** k_number
    return tot == int(number)
main()