"""
Simple example of class method.
The most common case of @classmethod use is providing alternative
methods of constructor apart from __init__(). 
"""


class AsciiArt:
    def __init__(self, characters):
        self._characters = characters

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r", encoding="utf-8") as f:
            characters = f.read()
            return cls(characters)

    def display(self):
        print(self._characters)


face1 = AsciiArt(":)")
face1.display()

face2 = AsciiArt.from_file("face.txt")
face2.display()
