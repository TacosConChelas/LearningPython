def main():
    time = str(input("What time is it? ")).strip()
    if "." in time:
        time = convert(time)

    hours, minutes = time.split(":")

    is_hours_correct(hours, minutes)



def convert(time):

    hours, minutes = time.split(".")
    minutes = int(minutes)

    minutes = int((minutes * 60) / 10)

    return hours + ":" + str(minutes)


def is_hours_correct(h, m):
    h = int(h)
    m = int(m)

    if (7 <= h <= 8):
        if (h == 8 and m != 0):
            return
        else:
            print("breakfast time")

    elif (12 <= h <= 13):
        if (h == 13 and m != 0):
            return
        else:
            print("lunch time")

    elif (18 <= h <= 19):
        if (h == 19 and m != 0):
            return
        else:
            print("dinner time")

    else:
        return


if __name__ == "__main__":
    main()
