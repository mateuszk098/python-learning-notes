"""
LetterSet naive test.
"""

from my_types import letter_set as ls


def main():

    s1 = ls.LetterSet()
    for letter in ["a", "a", "c", "d", "e", "f", "g"]:
        s1.add(letter)
    s1.print_out()

    s2 = ls.LetterSet()
    for letter in ["a", "a", "f", "t", "r", "z", "q"]:
        s2.add(letter)
    s2.print_out()

    s3 = s1 | s2
    s3.print_out()

    s4 = s1 & s2
    s4.print_out()


if __name__ == "__main__":
    main()
