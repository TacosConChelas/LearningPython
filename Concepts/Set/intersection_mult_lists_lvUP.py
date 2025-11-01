"""
Exercise 3 — Intersection of Multiple Lists

Given a list of lists of integers (e.g., [[1,2,3], [2,3,4], [2,5]]), return a sorted list of 
integers that appear in all lists (the intersection).
Goal: efficient for many lists and large sizes.

Hint: Convert the first list to a set and iteratively intersect with set() of each 
following list using .intersection_update() or &=.
"""
def intersection_items(list_of_lists: list[list[int]]) -> list[int]:
    """
    Return the sorted intersection of all sublists.
    """
    if not list_of_lists:
        return []

    # Compute intersection of all sets at once
    common = set.intersection(*map(set, list_of_lists))
    return sorted(common)


def main():
    list_of_lists = [
        [1, 2, 3],
        [2, 3, 4],
        [2, 5, 3],
        [2, 3, 7],
        [9, 1, 2, 4, 8, 3],
        [2, 1, 4, 3, 0],
    ]

    print(f"The final list is: {intersection_items(list_of_lists)}")


if __name__ == "__main__":
    main()
