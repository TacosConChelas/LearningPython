"""
2) Reverse a list without using .reverse() or slicing ([::-1]).
"""
def main():
    numbers_list = [1, 3, 4, 4, 6, 7, 8, 8, 9, 8]
    print(
        reverse_list(numbers_list)
        )
def reverse_list(lst : list) -> list:
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

if __name__ == "__main__":
    main()