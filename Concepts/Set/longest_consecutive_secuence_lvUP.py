"""
xercise 2 — Longest Consecutive Sequence

Given an unsorted array of integers, return the length of the longest consecutive elements sequence.
Example: [100, 4, 200, 1, 3, 2] → longest consecutive sequence is [1,2,3,4] so return 4.
Goal: O(n) expected time.

Hint: Put everything in a set. For each number that is a potential sequence start (num - 1 not in set), 
iterate forward counting num+1, num+2, ... until the sequence breaks.
"""
def longest_consecutive(nums: list[int]) -> int:
    """
    Return the length of the longest consecutive sequence in an unsorted list.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0
    best_sequence = []  # optional, for showing the actual numbers

    for num in num_set:
        # only start a new sequence if num-1 is not in the set
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            current_sequence = [num]

            # expand the sequence forward
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                current_sequence.append(current_num)

            # update the best sequence found
            if current_length > max_length:
                max_length = current_length
                best_sequence = current_sequence

    print(f"Longest consecutive sequence: {best_sequence}")
    print(f"Length: {max_length}")
    return max_length


def main():
    nums = [100, 4, 200, 1, 3, 2, 9, 11, 35, 69, 30]
    longest_consecutive(nums)


if __name__ == "__main__":
    main()
