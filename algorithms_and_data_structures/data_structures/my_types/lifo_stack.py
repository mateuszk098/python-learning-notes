"""
Example implementation of stack structure.
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
