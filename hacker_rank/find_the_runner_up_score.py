"""
See description at https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

Given the participants' score sheet for your University Sports Day, you are required 
to find the runner-up score. You are given n scores. Store them in a list and find 
the score of the runner-up.
"""

if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    # In set we have only unique values.
    larr = list(set(arr))
    result = sorted(larr)[-2]
    print(result)
