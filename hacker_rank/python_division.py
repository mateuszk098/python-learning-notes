"""
See description at https://www.hackerrank.com/challenges/python-division

The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines. The first line should contain the result of integer 
division, a // b. The second line should contain the result of float division, a / b.
No rounding or formatting is necessary.
"""


def main() -> None:
    a: int = int(input())
    b: int = int(input())

    print(a//b)
    print(a/b)


if __name__ == '__main__':
    main()
