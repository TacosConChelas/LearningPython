"""
"""
def main():
    while(True):
        intro_()
        try: 
            option = int(input("Select: "))
            match(option):
                case 7: break
        except : 
            continue


def intro_():
    print(r'    ______           _                              ')
    print(r'    | ___ \         (_)                             ')
    print(r'    | |_/ / __ _ ___ _  ___                         ')
    print(r'    | ___ \/ _` / __| |/ __|                        ')
    print(r'    | |_/ / (_| \__ \ | (__                         ')
    print(r'    \____/ \__,_|___/_|\___|                        ')
    print(r'                                                    ')
    print(r'     _____       _            _       _             ')
    print(r'    /  __ \     | |          | |     | |            ')
    print(r'    | /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ ')
    print(r"    | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|")
    print(r'    | \__/\ (_| | | (__| |_| | | (_| | || (_) | |   ')
    print(r'     \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   ')
    print(r"                                                    ")
    print(r"    V. 1                                            ")
    print(r"    from Adriel :D                                  ")
    print(r"    Welcome, select an option:                      ")
    print(r"    1) Plus                  2) Substrac            ")
    print(r"    3) Multiplication        4) Division            ")
    print(r"    5) Power                 6) Square root         ")
    print(r"    7) Exit                  8) Manual              ")
    print()
if __name__ == "__main__":
    main()