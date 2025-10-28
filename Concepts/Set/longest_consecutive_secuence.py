"""
xercise 2 — Longest Consecutive Sequence

Given an unsorted array of integers, return the length of the longest consecutive elements sequence.
Example: [100, 4, 200, 1, 3, 2] → longest consecutive sequence is [1,2,3,4] so return 4.
Goal: O(n) expected time.

Hint: Put everything in a set. For each number that is a potential sequence start (num - 1 not in set), 
iterate forward counting num+1, num+2, ... until the sequence breaks.
"""
def main():
    longest_sequence()

def longest_sequence() -> None:
    unsorted_list = {100, 4, 200, 1, 3, 2, 9, 11, 35, 69, 30}
    largest_sequense = []
    for i in range(len(unsorted_list)):
        # print(1)
        sequence = []
        num = list(unsorted_list)[i]
        if (num - 1) not in unsorted_list:
            # print(2)
            sequence.append(num)
            while True:
                if (num + 1) in unsorted_list:
                    num += 1
                    sequence.append(num)
                else:
                    break
        # print(largest_sequense)
        lenght = len(sequence)
        if largest_sequense == []:
            largest_sequense = lenght, sequence
        elif largest_sequense[0] < lenght:
            largest_sequense = lenght, sequence

    print(f"Largest sequence: {largest_sequense[1]}\nIt's lenght: {largest_sequense[0]}\nThe original list: {unsorted_list}")




    
    print()

# def make_sequence():



if __name__ == "__main__":
    main()
