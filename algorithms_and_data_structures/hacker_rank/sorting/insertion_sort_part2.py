"""
https://www.hackerrank.com/challenges/insertionsort2
"""


def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        j = i  # The 0, ..., i-1 elements are sorted.
        value = arr[j]
        while j > 0 and value < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = value
        print(*arr)


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)
