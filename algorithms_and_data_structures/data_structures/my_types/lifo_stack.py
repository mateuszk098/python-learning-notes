"""
Example implementation of the LIFO Stack.

A LIFO (last-in, first-out) stack is a data structure that stores a sequence
of elements and allows for the insertion of new elements at one end of the
stack (the "top") and the removal of elements from the same end (the "top").
The element that is inserted last is also the first one to be removed, hence
the name "last-in, first-out."

Some advantages of LIFO stacks include:

* Simplicity: LIFO stacks are a simple data structure that can be implemented
  with a minimal amount of code.

* Efficient insertion and removal: LIFO stacks allow for efficient insertion
  and removal of elements at the top of the stack, with a time complexity
  of O(1) (constant time) for both operations.

* Natural order: LIFO stacks preserve the order of the elements, making them
  a good choice for applications where the order of the elements is important.

Some disadvantages of LIFO stacks include:

* Limited flexibility: LIFO stacks only allow for the insertion of elements
  at the top and removal of elements from the top, and do not support other
  operations such as random access or element removal from the middle of the stack.

LIFO stacks are a good choice for applications that require the insertion
and removal of elements at one end of the data set, and where the order of
the elements is important. They are commonly used in programs that need to
track the state of a computation, such as in undo/redo functionality, and
in algorithms that require the maintenance of a "backtracking" history,
such as in recursive function calls.
"""


class LifoStack:
    """Provides basic example of the stack structure."""

    def __init__(self, size, stack_type):
        self.stack = list()
        self.size = size
        self.stack_type = type(stack_type())

    def clear(self):
        """Clear the stack."""
        self.stack.clear()

    def print(self, message=None):
        """Print the stack elements."""
        if message:
            print(message)
        if self.stack:
            print(f"{self.__class__.__qualname__}: [", end=" ")
            for element in self.stack:
                print(element, end=" ")
            print("]")

    def push(self, element):
        """Push a new element to the stack."""
        if not isinstance(element, self.stack_type):
            raise TypeError(
                f"Element must be '{self.stack_type.__qualname__}', "
                f"not '{element.__class__.__qualname__}'.")
        if len(self.stack) < self.size:
            self.stack.append(element)
        else:
            raise Exception("Stack Overflow.")

    def pop(self):
        """Pop an element from the stack."""
        if len(self.stack) > 0:
            return self.stack.pop()
        raise Exception("Stack is empty.")
