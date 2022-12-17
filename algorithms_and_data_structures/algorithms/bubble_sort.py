"""
Example implementation of the Bubble Sort O(N^2).
"""


def bubble_sort(array):
    """Returns sorted array, using the bubble sort algorithm."""
    length = len(array)
    if length <= 1:
        return
    for i in range(1, length):
        for j in range(length-1, i-1, -1):
            if array[j] < array[j-1]:
                value = array[j-1]
                array[j-1] = array[j]
                array[j] = value


l = [1, 5, 2, 2, 4, 6, 7, 12, 32, 5, 1, 35, 6]
bubble_sort(l)
print(l)
