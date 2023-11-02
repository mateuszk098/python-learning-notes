"""
See description at https://www.hackerrank.com/challenges/python-tuples/

Given an integer, n, and n space-separated integers as input, create 
a tuple, t, of those n integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n: int = int(input())
    t: tuple = tuple(map(int, input().split()))

    print(hash(t))  # Run with Pypy 3
