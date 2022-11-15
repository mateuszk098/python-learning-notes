"""
See description at https://www.hackerrank.com/challenges/python-loops

The provided code stub reads an integer, n, from STDIN. 
For all non-negative integers i < n, print i^2.
"""


def main() -> None:
    n: int = int(input())
    for i in range(n):
        print(i**2)


if __name__ == "__main__":
    main()
