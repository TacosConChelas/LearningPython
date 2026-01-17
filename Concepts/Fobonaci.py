def main():
    num = int(input("Enter the limit number of your fibonacy secuence: "))
    print(f"The last fibonaci number is {fibonaci(num)}")
    


def fibonaci(limit):
    numbers = [0, 1]
    if limit == 0:
        return []
    if limit == 1: 
        return 1
    for _ in range(limit):
        numbers.append(numbers[-1] + numbers[-2])
    # print(numbers)
    return numbers[-2]
if __name__ == "__main__":
    main()