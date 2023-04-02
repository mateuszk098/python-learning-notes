"""
See description at https://www.hackerrank.com/challenges/python-arithmetic-operators

The provided code stub reads two integers from STDIN, a and b. 
Add code to print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.
"""


def main() -> None:
    a: int = int(input())
    b: int = int(input())

    print(a+b)
    print(a-b)
    print(a*b)


if __name__ == "__main__":
    main()
