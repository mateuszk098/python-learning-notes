"""
Example implementation of queue structure.
"""


class FifoQueue:
    """Provides basic example of the queue structure."""

    def __init__(self, size, queue_type):
        self._queue = list()
        self._size = size
        self._queue_type = type(queue_type())
        self._length = 0

    def push(self, element):
        """Push a new element to the queue."""
        if not isinstance(element, self._queue_type):
            raise TypeError(
                f"Element must be '{self._queue_type.__qualname__}', "
                f"not '{element.__class__.__qualname__}'.")
        if self._length < self._size:
            self._queue.append(element)
            self._length += 1
        else:
            raise Exception("Queue is full.")

    def pop(self):
        """Pop the element from the queue."""
        if self._length != 0:
            element = self._queue.pop(0)
            self._length -= 1
            return element
        raise Exception("Queue is empty.")

    def is_empty(self):
        """Returns True if queue is empty, False otherwise."""
        return self._length == 0

    def print(self, message=None):
        """Print the queue elements."""
        if message:
            print(message)
        if self._length != 0:
            print(f"{self.__class__.__qualname__}: [", end=" ")
            for element in self._queue:
                print(element, end=" ")
            print("]")
