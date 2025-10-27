"""
1) Write a function that removes duplicate elements from a list without using set().
"""
def main():
    numbers_list = [1, 3, 4, 4, 6, 7, 8, 8, 9, 8]
    for number in numbers_list:
        count_number = numbers_list.count(number)
        if count_number > 1:
            for _ in range(count_number - 1):
                numbers_list.remove(number)
    print(numbers_list)
if __name__ == "__main__":
    main()