def main():
    while True:
        try:
            phrase = input("Fracction: ").strip()
            x, y = phrase.split("/")
            x, y = int(x), int(y)
            if (y <= 0) or (x > y) or (x <= 0):
                continue
            if (x <= 0):
                print("E")
                break
            percent = int((x / y) * 100)
            if percent >= 99:
                print("F")
                break
            else:
                print(f"{percent}%")
                break
        except:
            continue
main()