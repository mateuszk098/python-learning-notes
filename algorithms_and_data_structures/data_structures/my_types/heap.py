"""
Example implementation of the Heap.

A heap is a complete binary tree that satisfies the heap property,
which states that the value of each node in the tree is greater than
or equal to the values of its children. There are two types of heaps:
min heaps, in which the value of each node is less than or equal to the
values of its children, and max heaps, in which the value of each node
is greater than or equal to the values of its children.

Some advantages of heaps include:

* Efficient insertion and removal: Heaps allow for efficient insertion
  and removal of elements, with an average-case time complexity of O(log n)
  for both operations.

* Efficient retrieval of minimum/maximum element: In a min heap, the minimum
  element is always the root of the tree, and in a max heap, the maximum element
  is always the root of the tree. This allows for efficient retrieval of the
  minimum/maximum element in the heap, with a time complexity of O(1).

* Sorted data: Heaps store data in a sorted manner, which can be useful
  in certain applications.

Some disadvantages of heaps include:

* Limited flexibility: Heaps only support basic operations such as insertion,
  removal, and retrieval of the minimum/maximum element, and do not allow for
  other operations such as random access or element removal from the middle
  of the heap.

Heaps are a good choice for applications that require efficient insertion,
removal, and retrieval of the minimum/maximum element, and where the size
of the data set is not too large. They are commonly used in algorithms that
require the maintenance of a priority queue, such as in graph traversal
and sorting algorithms.
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
