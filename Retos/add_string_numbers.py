"""
num1 = "12349"
num2 = "46853"
num3 = "49656"

- add num1 + num2
- add the second number in num1 and the second number in num3
- change num2 into a float and print the type to the console as a float
"""
def main():
    num1 = "12349"
    num2 = "46853"
    num3 = "49656"

    print(int(num1) + int(num2))
    print(int(num1[1]) + int(num3[1]))
    print(type(float(num3)))    


if __name__ == "__main__":
    main()