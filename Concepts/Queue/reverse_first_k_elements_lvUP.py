"""
2 ----

Reverse the first K elements of a queue
Given a queue and a number k, reverse the order of the first k elements.
"""
from collections import deque

def reverse_first_k(queue: deque, k: int) -> deque:
    if k <= 0 or k > len(queue):
        return queue

    stack = []

    # Step 1: Pop first k elements from queue and push into stack
    for _ in range(k):
        stack.append(queue.popleft())

    # Step 2: Pop from stack and add back to queue (reversed order)
    while stack:
        queue.append(stack.pop())

    # Step 3: Move the remaining elements (n-k) to the back to maintain order
    for _ in range(len(queue) - k):
        queue.append(queue.popleft())

    return queue


def main():
    q = deque([9, 7, 6, 4, 3, 8, 9, 10])
    k = 4
    print("Original queue:", q)
    q = reverse_first_k(q, k)
    print("Modified queue:", q)

if __name__ == "__main__":
    main()
