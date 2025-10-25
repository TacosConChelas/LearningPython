def main():
    operation = str(input("Expression: ")).strip()
    x, sig, y = operation.split(" ")

    match sig:
        case "+":
            print(float(x) + float(y))
        case "-":
            print(float(x) - float(y))
        case "*":
            print(float(x) * float(y))
        case "/":
            if validation(y):
                total = float(x) / float(y)
                print(f"{total:.1f}")
            else:
                print("Invalid operation")
        case _:
            print("invalid operation")


def validation(y):
    return (y != 0)


main()