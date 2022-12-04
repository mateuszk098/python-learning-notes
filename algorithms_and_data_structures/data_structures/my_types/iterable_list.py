"""
Example implementation of iterable singly linked list.
The most important part of this example is to show `__iter__()` method,
so for full example of linked list see the singly_linked_list.py file.
"""


class Node:
    """A single node of the linked list. Contains
    value attribute and a pointer to the next node."""

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class MyIterator:

    def __init__(self, other):
        self.ptr = other.head

    def __next__(self):
        if self.ptr is not None:
            val = self.ptr.value
            self.ptr = self.ptr.next
            return val
        else:
            raise StopIteration


class IterableList:
    """A basic implementation of the Linked List structure."""

    def __init__(self):
        """Initialise a new object. Sets head and a tail pointer to None"""
        self.head = None
        self.tail = None
        self.length = 0

    def add_last(self, value):
        """Adds new value at the end of the list."""
        new_node = Node(value)
        if self.head is None:  # Empty list.
            self.head = new_node
            self.tail = new_node
        else:  # List contains some elements.
            self.tail.next = new_node  # type: ignore
            self.tail = new_node
        self.length += 1

    def print_out(self):
        """Prints elements of the list."""
        ptr = self.head
        if ptr is None:  # Empty list.
            return
        while ptr is not None:
            print(ptr.value, end=" ")
            ptr = ptr.next
        print()

    def __iter__(self):
        return MyIterator(self)
