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

class Stack():
    def __init__(self) -> None:
        self._queue1 = deque()
        self._queue2 = deque()
    
    def push(self, item) -> None:
        if self.is_empty():
            self._queue1.append(item) 
            return
        # print(f" 0 ------------------- {self._queue1} ------------------")
        for _ in range(len(self._queue1)):
            self._queue2.append(self._queue1.popleft())
        self._queue1.append(item)
        # print(f" 1 ------------------- {self._queue2} ------------------")
        for _ in range(len(self._queue2)):
            self._queue1.append(self._queue2.popleft())
        # print(f" 2 ------------------- {self._queue1} ------------------")
    
    def top(self):
        if self.is_empty():
            raise IndexError(f"{self.__repr__()} is empty")
        return self._queue1[0]        

    def pop(self):
        if self.is_empty():
            # return
            raise IndexError(f"{self.__repr__()} is empty")
        return self._queue1.popleft()

    def is_empty(self) -> bool:
        # print(f"empty {self._queue1}")
        return len(self._queue1) == 0

    
    def __repr__(self) -> str:
        return f"The Stack: {self._queue1}"
def main():
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop()) 
    print(s.top()) 
    
if __name__ == "__main__":
    main()