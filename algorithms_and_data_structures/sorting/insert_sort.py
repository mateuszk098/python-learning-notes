"""
Example implementation of the Insert Sort.

Insertion sort is an in-place sorting algorithm that builds the final sorted
array one element at a time. It is a simple sorting algorithm that works well
for small lists and partially sorted lists.

Time complexity: O(n^2)
Space complexity: O(1)

1. The algorithm starts by considering the first element in the list as being sorted.
2. Then, it looks at the next element in the list and compares it to the elements 
   that are already sorted.
3. If the next element is smaller than the element it is being compared to,
   it is inserted in its correct position in the sorted list.
4. This process is repeated for all the remaining elements in the list.
"""

from copy import copy


def insert_sort(array):
    """Returns sorted array, using the `Insert Sort` algorithm."""
    array_len = len(array)
    if array_len <= 1:
        return array

    for i in range(1, array_len):
        j = i  # The 0, ..., i-1 elements are sorted.
        value = array[j]
        while j > 0 and value < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = value

    return array


l1 = [1, 5, 2, 2, 4, 6, 7, 12, 32, 5, 1, 35, 6]
l1_sorted = insert_sort(copy(l1))

assert l1 == [1, 5, 2, 2, 4, 6, 7, 12, 32, 5, 1, 35, 6]
assert l1_sorted == [1, 1, 2, 2, 4, 5, 5, 6, 6, 7, 12, 32, 35]
