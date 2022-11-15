"""
See description at https://www.hackerrank.com/challenges/python-print

The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "" represents the consecutive values in between.
"""


if __name__ == "__main__":
    n: int = int(input())
    for i in range(n):
        print(i+1, end="")
