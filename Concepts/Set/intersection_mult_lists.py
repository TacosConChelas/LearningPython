"""
Exercise 3 — Intersection of Multiple Lists

Given a list of lists of integers (e.g., [[1,2,3], [2,3,4], [2,5]]), return a sorted list of 
integers that appear in all lists (the intersection).
Goal: efficient for many lists and large sizes.

Hint: Convert the first list to a set and iteratively intersect with set() of each 
following list using .intersection_update() or &=.
"""
from typing import Any


def main():
    list_of_lists = [[1,2,3], [2,3,4], [2,5, 3], [2, 3, 7],[9, 1, 2, 4, 8, 3], [2, 1, 4, 3, 0]]
    print(f"the final list is: {itersections_items(list_of_lists)}")

def itersections_items(list_of_lists : list[list]) -> list:
    final_list = set(list_of_lists[0])
    # print(final_list)
    for i in range(1, len(list_of_lists)):
        final_list = final_list.intersection(set(list_of_lists[i]))
    final_list = list(final_list)
    final_list.sort()
    return final_list
    

if __name__ == "__main__":
    main()