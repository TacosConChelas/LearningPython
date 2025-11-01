"""
Exercise 1 — Two Sum (set version)

Given an array of integers nums and an integer target, return True if there exist 
two numbers in nums that add up to target, otherwise return False.
Constraints: aim for O(n) time and O(n) extra space.
"""
def main():
    nums = [1, 3, 4, 6, 7, 8, 8, 9, 9, 1, 2, 6, 8, 3, 0, 3]
    target = 7
    print(f"For target: {target}, pair exist: {sum_two_numbers(nums, target)}")

def sum_two_numbers(numbers : list[int], target : int) -> bool:
    sum_equals = set()
    for num in numbers:
        if (target - num) in sum_equals:
            return True
        sum_equals.add(num)
    return False

if __name__ == "__main__":
    main() 