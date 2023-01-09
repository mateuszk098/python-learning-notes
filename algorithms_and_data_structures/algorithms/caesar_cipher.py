"""
Example of the Caesar cipher encoding.
"""


def encode(text, offset):
    result = []
    for letter in text:
        if letter.isupper():
            new_letter = chr((ord(letter) - ord("A") + offset) % 26 + ord("A"))
        else:
            new_letter = chr((ord(letter) - ord("a") + offset) % 26 + ord("a"))
        result.append(new_letter)
    return "".join(result)


def decode(text, offset):
    result = []
    for letter in text:
        if letter.isupper():
            new_letter = chr((ord(letter) - ord("A") - offset) % 26 + ord("A"))
        else:
            new_letter = chr((ord(letter) - ord("a") - offset) % 26 + ord("a"))
        result.append(new_letter)
    return "".join(result)


assert encode("abcdef", 1) == "bcdefg"
assert decode("bcdefg", 1) == "abcdef"
