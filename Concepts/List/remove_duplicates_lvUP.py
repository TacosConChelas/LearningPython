"""
1) Write a function that removes duplicate elements from a list without using set().
"""
def main():
    numbers_list = [1, 3, 4, 4, 6, 7, 8, 8, 9, 8]
    print(remove_duplicates_in(numbers_list))

def remove_duplicates_in(numbers_list : list) -> list:
    seen = set()
    result = []
    for num in numbers_list:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

if __name__ == "__main__":
    main()