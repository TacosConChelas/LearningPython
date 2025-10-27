"""
Reverse a list without using .reverse() or slicing ([::-1]).
"""
def main():
    numbers_list = [1, 3, 4, 4, 6, 7, 8, 8, 9, 8]
    print(
        [numbers_list[- (i + 1)] for i in range(len(numbers_list))]
        )
if __name__ == "__main__":
    main()