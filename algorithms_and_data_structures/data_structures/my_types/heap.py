"""
Example implementation of heap structure.
It is used to represent a priority queue.
"""


class Heap:
    """Provides basic example of the heap structure."""

    def __init__(self, size):
        self._length = 0
        self._heap = [0 for _ in range(size + 1)]

    def push(self, value):
        """Push a value to the heap."""
        self._length += 1
        self._heap[self._length] = value
        self._go_to_the_top()

    def pop(self):
        """Pop the value from the heap."""
        value = self._heap[1]
        self._heap[1] = self._heap[self._length]
        self._length -= 1
        self._go_to_the_bottom()
        return value

    def print(self, message=None):
        """Print the heap out."""
        if message:
            print(message)
        for index in range(1, self._length // 2 + 1):
            print(f"Parent: {self._heap[index]}", end=" ")
            print(f"Left Child: {self._heap[2 * index]}", end=" ")
            if 2 * index + 1 <= self._length:  # Right child can not exist.
                print(f"Right Child: {self._heap[2 * index + 1]}", end=" ")
            print()

    def _go_to_the_top(self):
        """Realise priority of the pushed value."""
        n = self._length
        value = self._heap[self._length]
        while n != 1 and self._heap[n // 2] <= value:
            self._heap[n] = self._heap[n // 2]
            n = n // 2
        self._heap[n] = value

    def _go_to_the_bottom(self):
        """Repair heap priorities after pop."""
        parent = 1
        while True:
            child = 2 * parent  # 2 * parent (left child), 2 * parent + 1 (right child).
            if child > self._length:
                break
            if child + 1 <= self._length:  # Right child can not exist.
                if self._heap[child] < self._heap[child + 1]:
                    child += 1
            if self._heap[parent] > self._heap[child]:
                break
            tmp = self._heap[child]
            self._heap[child] = self._heap[parent]
            self._heap[parent] = tmp
            parent = child
