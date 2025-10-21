def main():
    number = input("Enter a positive number: ").strip()
    try:
        if int(number) < 0:
            print("Invalid number")
        else:
            print(sum_digits(number))
    except:
        print("Invalid number entered")        
def sum_digits(number):
    sum = 0
    for n in [int(num) for num in number]:
        sum += n
    return sum
main()