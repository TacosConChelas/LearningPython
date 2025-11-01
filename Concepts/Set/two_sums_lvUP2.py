"""
Exercise 1 — Two Sum (set version)

Given an array of integers nums and an integer target, return True if there exist 
two numbers in nums that add up to target, otherwise return False.
Constraints: aim for O(n) time and O(n) extra space.
"""
def has_pair_with_sum(nums: list[int], target: int) -> bool:
    """
    Return True if there exist two numbers in nums that add up to target.
    Uses a hash set for O(n) time and O(n) space.
    """
    seen = set()  # stores numbers we've already processed
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False


def main():
    nums = [1, 3, 4, 6, 7, 8, 8, 9, 9, 1, 2, 6, 8, 3, 0, 3]
    target = 7
    print(f"For target={target}, pair exists: {has_pair_with_sum(nums, target)}")


if __name__ == "__main__":
    main()
