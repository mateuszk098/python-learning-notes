def print_formatted(number):
    # your code goes here

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


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
