"""
5) Combine two lists by alternating elements from each one (e.g., [1,2,3] and [a,b,c] → [1,a,2,b,3,c]).
"""
import numbers


def main():
    numbers = [1, 2, 3, 4, 5, 6, 8]
    letters = ["a", "b", "c", "d", "e", "f"]
    lenght_numbers, lenght_letters = len(numbers), len(letters)
    if lenght_letters > lenght_numbers:
        print(extended_list(letters, numbers, lenght_numbers))
        # print("1")

    elif lenght_letters < lenght_numbers:    
        print(extended_list(numbers, letters, lenght_letters))
        # print("2")
    else:
        print(extended_list(numbers, letters, lenght_numbers))
        # print("3")

def extended_list(list1 : list, list2 : list, lenght_2 : int) -> list:
    # lenght, large_list = ((lenght_numbers, 1) if lenght_numbers < lenght_letters else (lenght_letters, 2))
    # limite up: 12--- valores de i:  0, 2, 4, 6, 8, 10
    for i in range(0, (lenght_2 * 2), 2):
         list1.insert(i, list2.pop(0))

    return list1

if __name__ == "__main__":
    main()