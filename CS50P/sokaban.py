def main():

    history = []

    while True:
        action = input("Action: ")
        

        if action == "Undo":
            undone = history.pop()
            print(f"Undone {undone}")
        
        if action == "Restart":
            restart = history.clear()
            print(f"Restarted {restart}")
        else:
            history.append(action)

        print(history)


main()