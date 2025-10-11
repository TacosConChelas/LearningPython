def hello(name="User"):
    print("Hola ", name)

def main():
    hello()
    name = input("What's your name?")
    hello(name)

main()
