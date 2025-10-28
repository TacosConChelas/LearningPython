"""
Exercise 1 — Two Sum (set version)

Given an array of integers nums and an integer target, return True if there exist 
two numbers in nums that add up to target, otherwise return False.
Constraints: aim for O(n) time and O(n) extra space.
"""
def main():
    print(sum_two_numbers())

def sum_two_numbers() -> bool:
    nums = [1, 3, 4, 6, 7, 8, 8, 9, 9, 1, 2, 6, 8, 3, 0, 3]
    target = 7
    sum_equals = set()
    for num in nums:
        if (target - num) in sum_equals:
            return True
        else:
            sum_equals.add(num)
            # print(f"num: {num} and nums: {sum_equals}")
    return False

if __name__ == "__main__":
    main() 