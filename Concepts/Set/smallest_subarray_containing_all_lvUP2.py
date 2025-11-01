"""
Given an array arr, find the length of the smallest contiguous subarray that contains all 
distinct elements present in arr.
Example: arr = [a, b, c, a, b, c, b, a] — the set of unique elements is {a,b,c}; 
the smallest window containing all is [a,b,c] length = 3.
Goal: use set plus two-pointer / sliding window technique for near O(n) time.

Hint: First compute required = len(set(arr)). Then use sliding window with a dictionary of counts 
(or another structure) to know when the window contains all required distinct elements.
"""

def smallest_subarray_with_all_unique(arr):
    required = len(set(arr))
    window_counts = {}
    formed = 0
    left = 0
    min_length = float('inf')

    for right, x in enumerate(arr):
        window_counts[x] = window_counts.get(x, 0) + 1
        if window_counts[x] == 1:
            formed += 1

        while formed == required:
            min_length = min(min_length, right - left + 1)
            window_counts[arr[left]] -= 1
            if window_counts[arr[left]] == 0:
                formed -= 1
            left += 1

    return min_length


def main():
    arr = ['a', 'b', 'c', 'a', 'b', 'c', 'b', 'a']
    print(smallest_subarray_with_all_unique(arr))


if __name__ == "__main__":
    main()
