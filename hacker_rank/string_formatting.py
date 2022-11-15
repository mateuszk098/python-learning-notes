"""
See description at https://www.hackerrank.com/challenges/python-string-formatting

Given an integer, n, print the following values for each integer i from 1 to n:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
"""


def print_formatted(number):
    # your code goes here

    # Space is computed for binary representation because it has most characters.
    space = len(bin(number)) - 2  # Minus 2 because we discard 0b.

    for n in range(1, number+1):
        decimal = str(n)

        octal = str(oct(n))
        octal = octal.split("o")[1]

        hexadecimal = str(hex(n))
        hexadecimal = hexadecimal.split("x")[1]
        hexadecimal = hexadecimal.upper()

        binary = str(bin(n))
        binary = binary.split("b")[1]

        print(decimal.rjust(space, " "), end=" ")
        print(octal.rjust(space, " "), end=" ")
        print(hexadecimal.rjust(space, " "), end=" ")
        print(binary.rjust(space, " "))


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
