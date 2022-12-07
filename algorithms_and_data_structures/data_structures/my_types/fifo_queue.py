"""
Example implementation of queue structure.
"""


class FifoQueue:
    """Provides basic example of the queue structure."""

    def __init__(self, size, queue_type):
        self.queue = list()
        self.size = size
        self.queue_type = type(queue_type())
        self.length = 0

    def push(self, element):
        """Push a new element to the queue."""
        if not isinstance(element, self.queue_type):
            raise TypeError(
                f"Element must be '{self.queue_type.__qualname__}', "
                f"not '{element.__class__.__qualname__}'.")
        if self.length < self.size:
            self.queue.append(element)
            self.length += 1
        else:
            raise Exception("Queue is full.")

    def pop(self):
        """Pop the element from the queue."""
        if self.length != 0:
            element = self.queue.pop(0)
            self.length -= 1
            return element
        raise Exception("Queue is empty.")

    def is_empty(self):
        """Returns True if queue is empty, False otherwise."""
        return self.length == 0

    def print(self, message=None):
        """Print the queue elements."""
        if message:
            print(message)
        if self.length != 0:
            print(f"{self.__class__.__qualname__}: [", end=" ")
            for element in self.queue:
                print(element, end=" ")
            print("]")
