"""
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.
For example, a palindromic triangle of size 5 is:

1
121
12321
1234321
123454321

See description at https://www.hackerrank.com/challenges/triangle-quest-2/
"""

for number in range(1, int(input())+1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**number // 9)**2)
