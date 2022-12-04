"""
Example implementation of doubly linked list structure.

Methods:
* add_last()
* add_first()
* add_at()
* remove_last()
* remove_first()
* remove_at()
* get_at()
* reverse()
* print_forward()
* print_backward()
* remove_value()
* exist()
* add_with_sort()
"""


class Node:
    """A single node of the linked list. Contains
    value attribute and a pointers to the previous and next node."""

    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    """A basic implementation of the Linked List structure."""

    def __init__(self):
        """Initialise a new object. Sets head and a tail pointer to None"""
        self.head = None
        self.tail = None
        self.length = 0

    def add_last(self, value):
        """Adds a value at the end of the list."""
        new_node = Node(value)
        if self.head is None:  # Empty list.
            self.head = new_node
            self.tail = new_node
        else:  # List contains some elements.
            self.tail.next = new_node  # type: ignore
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def add_first(self, value):
        """Adds a value at the beginning of the list."""
        new_node = Node(value)
        if self.head is None:  # Empty list.
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def add_at(self, value, index):
        """Adds new value on the given index."""
        if index < 0 or index > self.length:
            raise IndexError("Index out of range.")
        if index == 0:
            self.add_first(value)
            return
        if index == self.length:
            self.add_last(value)
            return
        new_node = Node(value)
        current = self._iter_to(index)
        current.prev.next = new_node  # type: ignore
        new_node.prev = current.prev  # type: ignore
        new_node.next = current
        current.prev = new_node  # type: ignore
        self.length += 1

    def remove_last(self):
        """Removes the last element."""
        if self.tail is not None:
            self.tail = self.tail.prev
            self.tail.next = None  # type: ignore
            self.length -= 1

    def remove_first(self):
        """Removes the first element."""
        if self.head is not None:
            self.head = self.head.next
            self.head.prev = None  # type: ignore
            self.length -= 1

    def remove_at(self, index):
        """Removes element on the given index."""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        if index == 0:
            self.remove_first()
            return
        if index == self.length - 1:
            self.remove_last()
            return
        current = self._iter_to(index)
        current.prev.next = current.next  # type: ignore
        current.next.prev = current.prev  # type: ignore
        self.length -= 1

    def get_at(self, index):
        """Returns a value on the given index."""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        if index == 0 and self.head is not None:
            return self.head.value
        if index == self.length - 1 and self.tail is not None:
            return self.tail.value
        current = self._iter_to(index)
        return current.value  # type: ignore

    def remove_value(self, value):
        """Removes the given value from the list.
        Only the first found element will be removed."""
        current, found = self._search_ref(value)
        if not found:
            return
        self.length -= 1
        if self.length == 0:  # List has only one element.
            self.head = None
            self.tail = None
            return
        if self.head == current:  # Remove from the beginning.
            self.head = current.next
            current.next.prev = None
            return
        if self.tail == current:  # Remove from the end.
            current.prev.next = None
            self.tail = current.prev
        # Remove from somewhere in the middle.
        current.prev.next = current.next
        current.next.prev = current.prev

    def print_forward(self):
        """Prints the list from head to tail."""
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        print()

    def print_backward(self):
        """Prints the list from tail to head."""
        current = self.tail
        while current is not None:
            print(current.value, end=" ")
            current = current.prev
        print()

    def reverse(self):
        """Reverse the list."""
        if self.head is None:
            return
        current = self.head
        while current is not None:
            next = current.next
            current.next = current.prev
            current.prev = next
            current = next
        head = self.head
        self.head = self.tail
        self.tail = head

    def exist(self, value):
        """Returns True if the value exist, False otherwise."""
        _, found = self._search_ref(value)
        return found

    def add_with_sort(self, value):
        """Adds a new element with sorting. Works only if the list is sorted,
        or if you are using this as default `add()` function."""
        new_node = Node(value)
        self.length += 1

        if self.head is None:  # Empty list.
            self.head = new_node
            self.tail = new_node
            return

        # Find appropriate place.
        current = self.head
        while current is not None:
            if current.value >= value:
                break
            current = current.next

        if current.prev is None:  # Add at the beginning.
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            if current is None:  # Add at the end.
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:  # Add somewhere in the middle.
                current.prev.next = new_node
                new_node.prev = current.prev
                new_node.next = current
                current.prev = new_node

    def _iter_to(self, index):
        counts = 0
        current = self.head
        while counts < index:
            current = current.next  # type: ignore
            counts += 1
        return current

    def _search_ref(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current, True  # Found element.
            current = current.next
        return current, False  # Not found element.
