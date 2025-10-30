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
    i = 0
    arr_set = set()
    list_of_arrs = []
    for i in range(len(arr) - 1):
        if (arr[i + 1] - arr[i] == 1) or (arr[i + 1] == arr[i]):
            arr_set.add(arr[i])
            arr_set.add(arr[i + 1])
            print(f"1) {arr[i]} in {arr_set}")
        else:
            if list_of_arrs == []:
                list_of_arrs.append(arr_set)
                print(f"    1) {list_of_arrs}")

            elif len(list_of_arrs[0]) == len(arr_set): 
                list_of_arrs.append(arr_set)
                print(f"    2) {list_of_arrs}")
                
            elif len(list_of_arrs[0]) > len(arr_set):
                list_of_arrs.clear()
                list_of_arrs.append(arr_set)
                print(f"    3) {list_of_arrs}")
                
            print(f"2) {arr[i]} in {arr_set}")
            arr_set.clear()
            continue
    print(f"the smallest(s) subarray: {list_of_arrs} and it's length: {len(list_of_arrs[0])}")

if __name__ == "__main__":
    main()
