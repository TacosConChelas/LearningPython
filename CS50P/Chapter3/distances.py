distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pionner 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def convert(au):
    return au * 149597870700


def main():
    # for distance in distances.values():
    spacecraft = input("enter a spacecraft: ")
    print(f"{spacecraft} AU is {convert(distances[spacecraft])} in mts")



main()