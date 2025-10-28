"""
Exercise 5 — Smallest Subarray Containing All Unique Elements

Given an array arr, find the length of the smallest contiguous subarray that contains all 
distinct elements present in arr.
Example: arr = [a, b, c, a, b, c, b, a] — the set of unique elements is {a,b,c}; 
the smallest window containing all is [a,b,c] length = 3.
Goal: use set plus two-pointer / sliding window technique for near O(n) time.

Hint: First compute required = len(set(arr)). Then use sliding window with a dictionary of counts 
(or another structure) to know when the window contains all required distinct elements.
"""
from re import sub


def main():
    the_smallest_array()

def the_smallest_array():
    arr = [1, 2, 4, 5, 6, 11, 12, 13, 37, 38, 49, 50, 51]
    length = len(arr)
    i = 0
    arr_set = set()
    while i < len(arr):
        print(i)
        # print(1)
        arr_set.add(arr[i])
        while i < (len(arr) - 1):
            print(i)
            # print(2)
            if (arr[i + 1] - arr[i] == 1):
                arr_set.add(arr[i + 1])
                i += 1
            else:
                i += 1
                break
        if length > len(arr_set):
            length = len(arr_set)
        
        i += 1
    print(f"the smallest subarray: {arr_set} and it's length: {length}")
        
        


    




if __name__ == "__main__":
    main()
