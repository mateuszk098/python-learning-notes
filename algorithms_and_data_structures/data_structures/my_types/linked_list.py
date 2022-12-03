"""
Example implementation of singly linked list structure.
"""


class Node:
    """A single node of the linked list. Contains
    value attribute and a pointer to the next node."""

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
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

    def add_first(self, value):
        """Adds new value at the beginning of the list."""
        new_node = Node(value)
        if self.head is None:  # Empty list.
            self.head = new_node
            self.tail = new_node
        else:  # List contains some elements.
            new_node.next = self.head
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
        prev, current = self._iter_to(index)
        new_node = Node(value)
        prev.next = new_node  # type: ignore
        new_node.next = current
        self.length += 1

    def remove_last(self):
        """Removes the last element of the list."""
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        ptr = self.head
        while ptr.next.next is not None:  # type: ignore
            ptr = ptr.next  # type: ignore
        ptr.next = None  # type: ignore
        self.tail = ptr
        self.length -= 1

    def remove_first(self):
        """Removes the first element of the list."""
        if self.head is not None:
            self.head = self.head.next
            self.length -= 1

    def remove_at(self, index):
        """Removes element of the list on the given index."""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        if index == 0:
            self.remove_first()
            return
        if index == self.length - 1:
            self.remove_last()
            return
        prev, current = self._iter_to(index)
        prev.next = current.next  # type: ignore
        self.length -= 1

    def get_at(self, index):
        """Returns a value on the given index."""
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        if index == 0 and self.head is not None:
            return self.head.value
        if index == self.length - 1 and self.tail is not None:
            return self.tail.value
        _, current = self._iter_to(index)
        return current.value  # type: ignore

    def reverse(self):
        """Reverse the list."""
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def print_out(self):
        """Prints elements of the list."""
        ptr = self.head
        if ptr is None:  # Empty list.
            return
        while ptr is not None:
            print(ptr.value, end=" ")
            ptr = ptr.next
        print()

    def exist(self, value) -> bool:
        """Returns True if the element exists, otherwise returns False."""
        ptr = self.head
        while ptr is not None:
            if ptr.value == value:
                return True
            ptr = ptr.next
        return False

    def add_with_sort(self, value):
        """Adds a new element with sorting. Works only if the list is sorted,
        or if you are using this as default `add()` function."""
        new_node = Node(value)
        self.length += 1

        if self.head is None:  # Empty list.
            self.head = new_node
            self.tail = new_node
            return

        prev = None
        current = self.head
        while current is not None:  # Find appropriate place.
            if current.value >= value:
                break
            else:
                prev = current
                current = current.next

        if prev is None:  # Add element at the beginning.
            self.head = new_node
            new_node.next = current
        else:
            if current is None:  # Add element at the end.
                prev.next = new_node
                self.tail = new_node
            else:  # Add element somewhere in the middle.
                prev.next = new_node
                new_node.next = current

    def remove_value(self, value):
        """Removes the given values from the list.
        Only the first found element will be removed."""
        prev, current, found = self._search_ref(value)
        if not found:
            return
        self.length -= 1
        if self.length == 0:  # List has only one element.
            self.head = None
            self.tail = None
            return
        if self.head == current:  # Remove from the beginning.
            self.head = current.next
            return
        if self.tail == current:  # Remove from the end.
            self.tail = prev
            prev.next = None
            return
        prev.next = current.next  # Remove from somewhere in the middle.

    def _iter_to(self, index):
        """Iterates `index` times. Returns tuple of current and previous pointers,
        where current is related to the element on the given index."""
        counts = 0
        prev = None
        current = self.head
        while counts < index:
            counts += 1
            prev = current
            current = current.next  # type: ignore
        return prev, current

    def _search_ref(self, value):
        """Searches for the given value and the previous value references.
        Returns a tuple with these pointers and True if found the given value,
        or False otherwise."""
        prev = None
        current = self.head
        while current is not None:
            if current.value == value:
                return prev, current, True  # Found given element.
            prev = current
            current = current.next
        return prev, current, False  # Not found given element.


# SLOW BUT DO NOT MODIFY L1.
def safe_concat(l1, l2):
    """Cocatenate two lists."""
    new_list = LinkedList()
    ptr1 = l1.head
    ptr2 = l2.head

    while ptr1 is not None:
        new_list.add_last(ptr1.value)
        ptr1 = ptr1.next

    while ptr2 is not None:
        new_list.add_last(ptr2.value)
        ptr2 = ptr2.next

    return new_list


# FAST BUT MODIFY L1 !!!
def fast_concat(l1, l2):
    """Fast concatenation of two lists. Modify `l1` instance."""
    new_list = l1
    new_list.head = l1.head
    new_list.tail.next = l2.head
    new_list.tail = l2.tail
    return new_list


# MODERATE BUT MODIFY L1 AND L2 TOO !!!
def concat_and_sort(l1, l2):
    """Cocatenate two sorted lists. Returns sorted concatenated list.
    Modify `l1` and `l2` instances."""

    new_list = LinkedList()
    new_list.length = l1.length + l2.length
    new_list.head = _sort(l1.head, l2.head)  # MODIFY POINTERS

    if l1.head is None:
        new_list.tail = l2.tail
    elif l2.head is None:
        new_list.tail = l1.tail
    else:
        if l1.tail is None:
            new_list.tail = l1.tail
        else:
            new_list.tail = l2.tail
    return new_list


def _sort(ptr1, ptr2):
    """Returns pointer, which point to the concatenated sorted list."""
    if ptr1 is None:
        return ptr2
    if ptr2 is None:
        return ptr1
    if ptr1.value <= ptr2.value:
        ptr1.next = _sort(ptr1.next, ptr2)
        return ptr1
    else:
        ptr2.next = _sort(ptr2.next, ptr1)
        return ptr2
