months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
def main():
    ## aun se puede mejorar más y optimizar, aun no lo está
    while True:
        date = str(input("Date: ")).strip().title()
        if (date[0] in [m[0] for m in months]) and (date[-6] == ",") and (date.count(" ") == 2):
            # se espera recibir algo asi: "September 8, 1636"    ----> comiensa con una letra, tiene 2 espacios y una coma
            # print("option 1")
            result = format_worlds(date)   
            if result is not None:
                print(result)
                break
        elif (date[0] in "1234567890") and (date.count("/") == 2):
            # se espera recibir algo asi: "9/8/1636"    ----> tiene 2 "/" y ninguna letra
            # print("option 2")
            result = format_numbers(date)
            if result is not None:
                print(result)    
                break
        # print("else")
def format_worlds(date):
    month_day, year = date.split(",")
    year = year.strip()
    month, day = month_day.split(" ")
    month = int(months.index(month)) + 1
    year, month, day = int(year), int(month), int(day)
    if (1 <= day <= 31) and (month is not None) and (1 <= month <= 12):
        if day <= 9:
            day = str(f"0{day}") 
        if month <= 9:
            month = str(f"0{month}")
        return f"{year}-{month}-{day}"
    else:
        return 

def format_numbers(date):
    month, day, year = date.split("/")    
    year, month, day = int(year), int(month), int(day)
    # print("option 2.1", f"{year}-{month}-{day}")
    if (1 <= month <= 12) and (1 <= day <= 31):
        # print("option 2.2")
        if day <= 9:
            day = str(f"0{day}") 
        if month <= 9:
            month = str(f"0{month}")
        return f"{year}-{month}-{day}"
    else:
        return

main()