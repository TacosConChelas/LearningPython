class CircularQueue:
    """Ring buffer con capacidad fija y opción de sobrescritura."""

    def __init__(self, capacity: int, overwrite: bool = False):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self._buf = [None] * capacity
        self._capacity = capacity
        self._head = 0
        self._tail = 0
        self._size = 0
        self._overwrite = overwrite          # True → sobrescribe al estar llena

    # ---------- operaciones básicas ----------
    def enqueue(self, item):
        if self._size == self._capacity:
            if not self._overwrite:
                raise OverflowError("Circular queue is full")
            # sobrescribir: avanzar head para descartar el más viejo
            self._head = (self._head + 1) % self._capacity
            self._size -= 1                 # compensamos el decremento posterior
        self._buf[self._tail] = item
        self._tail = (self._tail + 1) % self._capacity
        # alternativa 2 SOLO SI EL CASO REQUIERE AVANZAR 1 POSICION: 
        # self._tail = 0 if (self._tail + 1) == self._capacity else self._tail + 1 

        # El modulo % siempre hace que cuando tail se pase de capacility, tail se vuelva a reinciar

        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise IndexError("Circular queue is empty")
        item = self._buf[self._head]
        self._buf[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return item

    def peek(self):
        if self._size == 0:
            raise IndexError("Circular queue is empty")
        return self._buf[self._head]

    # ---------- utilidades ----------
    def __len__(self):
        return self._size

    def is_full(self):
        return self._size == self._capacity

    def is_empty(self):
        return self._size == 0

    def clear(self):
        self._buf = [None] * self._capacity
        self._head = self._tail = self._size = 0

    # ---------- representación e iteración ----------
    def __repr__(self):
        if self._size == 0:
            return f"CircularQueue([])"
        items = list(self)                # usa __iter__
        return f"CircularQueue({items})"

    def __iter__(self):
        idx = self._head
        cnt = 0
        while cnt < self._size:
            yield self._buf[idx]
            idx = (idx + 1) % self._capacity
            cnt += 1

def main():
    # Cola que lanza error al overflow
    cq1 = CircularQueue(3)
    cq1.enqueue('a'); cq1.enqueue('b'); cq1.enqueue('c')
    print(cq1)          # CircularQueue(['a', 'b', 'c'])
    # cq1.enqueue('d')  # <-- OverflowError

    # Cola que sobrescribe automáticamente
    cq2 = CircularQueue(3, overwrite=True)
    for ch in 'abcd':
        cq2.enqueue(ch)
    print(cq2)          # CircularQueue(['b', 'c', 'd'])  ← 'a' fue descartada

if __name__ == "__main__":
    main()