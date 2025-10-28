"""
Exercise 4 — Find Unique Element (XOR alternative with sets)

Given an array where every element appears twice except for one element which appears once, 
return that single one. (This is classic using XOR in O(n) time and O(1) space, but here implement using set.)
Goal: show set usage; complexity will be O(n) time but O(n) space.

Hint: Use a set to add/remove: if a number is not in the set add it, else remove it; 
at the end the set will contain the single number.
"""
def main():
    elements_list = [2, 3, 4, 3, 4, 2, 6, 6, 7, 7, 8, 8, 9, 9, 12, 13, 12 , 13, 1]
    elements_set = set()
    for element in elements_list:
        if element in elements_set:
            elements_set.remove(element)
        else:
            elements_set.add(element)
    print(elements_set)

if __name__ == "__main__":
    main()