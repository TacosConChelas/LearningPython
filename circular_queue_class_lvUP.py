"""
1) ----
Exercise 1 — Implement a Circular Queue

Description:
    Design a circular queue class (fixed size).
Implement:
    enqueue(item)
    dequeue()
s    front() → returns the front item
    rear() → returns the last item
    is_empty()
    is_full()
"""
import queue


class CircularQueue():
    def __init__(self, capacility: int) -> None:
        self._buff = [None] * capacility
        self._capacity = capacility
        self._size = 0
        self._tail = 0
        self._head = 0
    
    def enqueue(self, item) -> None:
        if self.is_full():
            return
        self._buff[self._tail] = item
        self._tail = (self._tail + 1) % self._capacity
        self._size += 1
        # print(f"size: {self._size}, tail: {self._tail}, {self._buff}")
    
    def dequeue(self):
        if self.is_empty():
            return
        item = self._buff[self._head]
        self._buff[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        # print(f"size: {self._size}, head: {self._head}, {self._buff}")
        return item
    
    def front(self):
        if self.is_empty():
            return
        return self._buff[self._head]
    
    def rear(self):
        if self.is_empty():
            return
        # print(self._tail)
        return self._buff[self._tail - 1]

    def is_empty(self):
        print(f"the object {self._buff} is empty")
        return self._size == 0
    
    def is_full(self):
        print(f"The object {self._buff} is full")
        return self._size == self._capacity
        # print(self._size)    
        
def main():
    q = CircularQueue(3)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print()
    print(q.is_full())
    print(q.dequeue())
    q.enqueue(40)
    # print(q._buff)
    print(q.front())
    print(q.rear())

if __name__ == "__main__":
    main()

        
