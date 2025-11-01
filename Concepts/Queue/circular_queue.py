class CircularQueue:
    """Cola circular de tamaño fijo."""
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("La capacidad debe ser > 0")
        self._buf = [None] * capacity   # búfer interno
        self._capacity = capacity
        self._head = 0                  # índice del primer elemento válido
        self._tail = 0                  # índice donde se insertará el próximo (el que será añadido con enqueue).
        self._size = 0                  # número de elementos actuales (0 ≤ _size ≤ _capacity).

    def enqueue(self, item):
        """Inserta un elemento al final de la cola.
        Si la cola está llena, lanza OverflowError (puedes cambiar la política)."""
        if self._size == self._capacity:
            raise OverflowError("Cola circular llena")
        self._buf[self._tail] = item
        self._tail = (self._tail + 1) % self._capacity
        self._size += 1

    def dequeue(self):
        """Elimina y devuelve el elemento más antiguo.
        Si está vacía, lanza IndexError."""
        if self._size == 0:
            raise IndexError("Cola circular vacía")
        item = self._buf[self._head]
        self._buf[self._head] = None           # opcional: liberar referencia
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return item

    def peek(self):
        """Devuelve el elemento al frente sin eliminarlo."""
        if self._size == 0:
            raise IndexError("Cola circular vacía")
        return self._buf[self._head]

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size == 0:
            return "CircularQueue([])"
        # Construir una vista ordenada para depuración
        items = []
        idx = self._head
        for _ in range(self._size):
            items.append(self._buf[idx])
            idx = (idx + 1) % self._capacity
        return f"CircularQueue({items})"