def main():
    greeting = str(input("Greeting: ")).strip()


    greeting = greeting.lower().split(" ")

    # print(greeting)
    # hello = greeting[0]

    if (greeting[0] == "hello" or greeting[0] == "hello,"):
        print("$0")
    elif greeting[0].startswith("h"):
        print("$20")
    else:
        print("$100")



main()
