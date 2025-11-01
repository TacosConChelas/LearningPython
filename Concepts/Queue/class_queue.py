"""
1 ---
Implement a Queue class using deque

Define your own methods: enqueue, dequeue, peek, is_empty.
"""
from collections import deque

class Queue():
    def __init__(self) -> None:
        # Creating a Queue object called "queue" inside Queue class, we can use it like a deque()
        self.queue = deque()
    
    def enqueue(self, item) -> None:
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.popleft()
    
    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def size(self):
        return len(self.queue)

def main():
    q = Queue()
    print(q.is_empty())
    q.enqueue("Apple")
    print(f"The size of our Queue: {q.size()} and its peek is {q.peek()}")
    q.dequeue()
    print(f"The size of our Queue: {q.size()}")

if __name__ == "__main__":
    main()
    
