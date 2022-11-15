"""
See description at https://www.hackerrank.com/challenges/py-set-add

Rupal has a huge collection of country stamps. She decided to count the 
total number of distinct country stamps in her collection. She asked for 
your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n = int(input().strip())
    stamps = set()

    for _ in range(n):
        stamp = input().strip()
        stamps.add(stamp)

    print(len(stamps))
