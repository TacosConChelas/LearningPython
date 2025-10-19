def main():
    dict = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0
    try:
        while True:
            item = str(input("Item: ")).strip().title()
            item = dict.get(item)
            if item is not None:
                total += item
                print(f"Total: ${total:.2f}")
            else:
                print("", end="")
    except EOFError:
        return
main()