"""
Example implementation of the Bubble Sort.

Bubble sort is a simple sorting algorithm that repeatedly iterates through
a list, compares adjacent elements, and swaps them if they are in the wrong order.
The algorithm repeats this process until it makes a pass through the list
without making any swaps, which indicates that the list is sorted.

Time complexity: O(n^2)
Space complexity: O(1)
"""

from copy import copy


def bubble_sort(array):
    """Returns sorted array, using the `Bubble Sort` algorithm."""
    array_len = len(array)
    if array_len <= 1:
        return array

    for i in range(1, array_len):
        for j in range(array_len - 1, i - 1, -1):  # Backward loop to not repeat comparisions.
            if array[j] < array[j - 1]:  # Swap these values.
                value = array[j - 1]
                array[j - 1] = array[j]
                array[j] = value

    return array


l1 = [1, 5, 2, 2, 4, 6, 7, 12, 32, 5, 1, 35, 6]
l1_sorted = bubble_sort(copy(l1))

assert l1 == [1, 5, 2, 2, 4, 6, 7, 12, 32, 5, 1, 35, 6]
assert l1_sorted == [1, 1, 2, 2, 4, 5, 5, 6, 6, 7, 12, 32, 35]
