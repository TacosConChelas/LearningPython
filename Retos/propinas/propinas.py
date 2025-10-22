def main():
    total = float(input("Enter the total: ").strip())
    percent = float(input("Enter the percent: ").strip())
    print(tip(total, percent))
def tip(total, percent):
    return round((total * percent) / 100, 2)
main()