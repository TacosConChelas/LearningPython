def main():
    space = get_pace(miles=26.2, minutes=0)
    print(f"You nedd to ron each mile in {round(space, 2)} minutes")

def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Invalid value for minutes")

    return minutes / miles

main()