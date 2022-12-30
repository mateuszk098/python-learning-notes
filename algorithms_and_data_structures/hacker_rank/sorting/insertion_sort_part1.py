"""
https://www.hackerrank.com/challenges/insertionsort1
"""


def insertionSort1(n, arr):
    # Write your code here
    i = n - 1
    val = arr[-1]
    while i > 0 and val < arr[i - 1]:
        arr[i] = arr[i - 1]
        i -= 1
        print(*arr)
    arr[i] = val
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
