"""
5) Combine two lists by alternating elements from each one (e.g., [1,2,3] and [a,b,c] → [1,a,2,b,3,c]).

built-in functions
"""
def main():
    numbers = [1, 2, 3, 4, 5, 6, 8]
    letters = ["a", "b", "c", "d", "e", "f"]
    print(merge_alternately(numbers, letters))

def merge_alternately(list1, list2):
    merged = []
    for a, b in zip(list1, list2):
        merged.extend([a, b])
    # Add remaining elements (if lists differ in length)
    merged.extend(list1[len(list2):])
    merged.extend(list2[len(list1):])
    return merged

if __name__ == "__main__":
    main()