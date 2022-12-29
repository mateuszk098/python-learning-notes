"""
Example implementation of the Set.

A set is a data structure that stores a collection of elements and allows for
the efficient checking of membership (i.e., whether an element is present in
the set) and insertion and deletion of elements. Sets do not store duplicate
elements, and the order of the elements is not preserved.

Some advantages of sets include:

* Efficient membership checking: Sets allow for efficient membership checking,
  with a time complexity of O(1) (constant time) on average.

* No duplicate elements: Sets do not store duplicate elements, making them a good
  choice for applications that require unique elements.

* Flexibility: Sets can be implemented using a variety of underlying data structures,
  such as arrays, linked lists, or trees, depending on the specific requirements
  of the application.

Some disadvantages of sets include:

* Limited support for element ordering: Sets do not preserve the order of the elements,
  and do not provide efficient access to the elements in a specific position.

* Poor performance with large data sets: Sets can become inefficient for large data sets,
  as the time complexity of the insert and delete operations is typically O(n)
  (linear time), which means that the time required to perform these operations
  increases as the size of the set grows.

Sets are a good choice for applications that require the efficient checking of membership
and the insertion and deletion of elements, and where duplicate elements are not allowed.
They are commonly used in programs that need to store and manipulate unique elements,
such as in database indexing and spelling checkers.
"""


class LetterSet:
    """Set of a-z letters."""

    def __init__(self):
        self.vals = [False for _ in range(26)]  # True means that letter is in the set.

    def add(self, letter):
        """Add a letter to the set."""
        index = self._to_index(letter)
        if index in range(26):
            self.vals[index] = True
        else:
            print("Letter beyond the alphabet.")

    def __or__(self, other):
        if not isinstance(other, LetterSet):
            raise NotImplemented
        set_sum = LetterSet()
        for index in range(26):
            set_sum.vals[index] = self.vals[index] or other.vals[index]
        return set_sum

    def __and__(self, other):
        if not isinstance(other, LetterSet):
            raise NotImplemented
        set_sum = LetterSet()
        for index in range(26):
            set_sum.vals[index] = self.vals[index] and other.vals[index]
        return set_sum

    def remove(self, letter):
        """Remove a letter from the set."""
        index = self._to_index(letter)
        if index != -1 and self.vals[index]:
            self.vals[index] = False
        else:
            print(f"Set does not contain {letter}.")

    def print_out(self):
        """Print out the set."""
        print("{", end=" ")
        for index in range(26):
            if self.vals[index]:
                print(f"{chr(index+65)} ", end="")
        print("}")

    def _to_index(self, letter):
        """Convert letter to number 0-25."""
        if "A" <= letter <= "Z" or "a" <= letter <= "z":
            return ord(letter.upper()) - ord("A")
        return -1  # Character beyond the alphabet.
