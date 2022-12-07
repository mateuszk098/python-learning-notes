"""
Example implementation of set structure.
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
