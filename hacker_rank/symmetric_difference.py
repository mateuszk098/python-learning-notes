"""
See description at https://www.hackerrank.com/challenges/symmetric-difference

Given 2 sets of integers, M and N, print their symmetric difference in 
ascending order. The term symmetric difference indicates those values that
 exist in either M or N but do not exist in both.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    _ = input()
    my_set1: set = set(map(int, input().strip().split()))
    _ = input()
    my_set2: set = set(map(int, input().strip().split()))
    symm_diff: list = sorted(my_set1 ^ my_set2)
    print(*symm_diff, sep="\n")
