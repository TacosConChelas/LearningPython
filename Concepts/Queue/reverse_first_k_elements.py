"""
2 ----

Reverse the first K elements of a queue
Given a queue and a number k, reverse the order of the first k elements.
"""
from collections import deque
def main():
    queue = [9, 7, 6, 4, 3, 8, 9, 10]
    queue = deque(queue)
    k_number = 4
    for _ in range(k_number):
        queue.append(queue.popleft())
    print(" ".join(str(item) for item in queue))


if __name__ == "__main__":
    main()