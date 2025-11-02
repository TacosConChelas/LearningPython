"""
Exercise 2 — Implement a Stack Using Two Queues

Description:
Create a Stack class that uses two queues (deques) internally.
Implement:
    push(x)
    pop()
    top()
    is_empty()
"""
from collections import deque

class Stack:
    """
    Stack implemented using two queues (FIFO structures).
    The most recent element is always kept at the front of _q1 for O(1) pop().
    Push operation costs O(n).
    """
    def __init__(self) -> None:
        self._q1 = deque()
        self._q2 = deque()

    def push(self, item) -> None:
        """Push an item onto the stack."""
        self._q2.append(item)
        while self._q1:
            self._q2.append(self._q1.popleft())
        # Swap roles
        self._q1, self._q2 = self._q2, self._q1

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._q1.popleft()

    def top(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._q1[0]

    def is_empty(self) -> bool:
        return len(self._q1) == 0

    def size(self) -> int:
        return len(self._q1)

    def __len__(self) -> int:
        return self.size()

    def __repr__(self) -> str:
        return f"Stack({list(self._q1)})"


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)
    print("Top:", s.top())  # 3
    print("Popped:", s.pop())  # 3
    print("After pop:", s)
    print("Empty?", s.is_empty())
    print("Size:", s.size())

if __name__ == "__main__":
    main()