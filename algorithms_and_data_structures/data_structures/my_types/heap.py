"""
Example implementation of heap structure.
It is used to represent a priority queue.
"""


class Heap:
    """Provides basic example of the heap structure."""

    def __init__(self, size):
        self.length = 0
        self.heap = [0 for _ in range(size + 1)]

    def push(self, value):
        """Push a value to the heap."""
        self.length += 1
        self.heap[self.length] = value
        self._go_to_the_top()

    def pop(self):
        """Pop the value from the heap."""
        value = self.heap[1]
        self.heap[1] = self.heap[self.length]
        self.length -= 1
        self._go_to_the_bottom()
        return value

    def print(self, message=None):
        """Print the heap out."""
        if message:
            print(message)
        for index in range(1, self.length // 2 + 1):
            print(f"Parent: {self.heap[index]}", end=" ")
            print(f"Left Child: {self.heap[2 * index]}", end=" ")
            if 2 * index + 1 <= self.length:  # Right child can not exist.
                print(f"Right Child: {self.heap[2 * index + 1]}", end=" ")
            print()

    def _go_to_the_top(self):
        """Realise priority of the pushed value."""
        n = self.length
        value = self.heap[self.length]
        while n != 1 and self.heap[n // 2] <= value:
            self.heap[n] = self.heap[n // 2]
            n = n // 2
        self.heap[n] = value

    def _go_to_the_bottom(self):
        """Repair heap priorities after pop."""
        parent = 1
        while True:
            child = 2 * parent  # 2 * parent (left child), 2 * parent + 1 (right child).
            if child > self.length:
                break
            if child + 1 <= self.length:  # Right child can not exist.
                if self.heap[child] < self.heap[child + 1]:
                    child += 1
            if self.heap[parent] > self.heap[child]:
                break
            tmp = self.heap[child]
            self.heap[child] = self.heap[parent]
            self.heap[parent] = tmp
            parent = child
