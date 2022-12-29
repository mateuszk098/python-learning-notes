"""
Example implementation of the FIFO Queue.

A FIFO (first-in, first-out) queue is a data structure that stores a sequence
of elements and allows for the insertion of new elements at one end of the queue
(the "rear") and the removal of elements from the other end (the "front").
The element that is inserted first is also the first one to be removed, hence
the name "first-in, first-out."

Some advantages of FIFO queues include:

* Simplicity: FIFO queues are a simple data structure that can be implemented with
  a minimal amount of code.

* Efficient insertion and removal: FIFO queues allow for efficient insertion and
  removal of elements at the front and rear of the queue, respectively.

* Natural order: FIFO queues preserve the order of the elements, making them a good
  choice for applications where the order of the elements is important.

Some disadvantages of FIFO queues include:

* Limited flexibility: FIFO queues only allow for the insertion of elements at the
  rear and removal of elements from the front, and do not support other operations
  such as random access or element removal from the middle of the queue.

FIFO queues are a good choice for applications where the order of the elements
is important, and where the main operations required are the insertion of elements
at one end of the queue and the removal of elements from the other end. They are
commonly used in situations where elements need to be processed in the order in which
they were received, such as in task scheduling or message processing.
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
