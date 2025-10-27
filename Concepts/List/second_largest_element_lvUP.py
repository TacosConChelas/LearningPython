"""
3) Find the second largest number in a list of integers.
"""
def main():
   numbers_list = [1, 3, 4, 4, 6, 7, 8, 8, 9, 8]
   print(second_largest(numbers_list))
   
def second_largest(numbers_list):
    first = second = float('-inf')
    for num in numbers_list:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second

if __name__ == "__main__":
    main()