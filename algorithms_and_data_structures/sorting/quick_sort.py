"""
Example implementation of the Quick Sort.

Quick sort is a divide-and-conquer sorting algorithm that works by partitioning
a list into two sublists, sorting the sublists, and then merging them back
together. It is a fast and efficient sorting algorithm, making it one of the
most popular sorting algorithms in use today.
    
Time complexity: O(n*log(n))
Space complexity: O(n)

1. The algorithm selects a pivot element from the list. This element is used
   to partition the list into two sublists.
2. All the elements in the first sublist are smaller than the pivot element,
   and all the elements in the second sublist are larger than the pivot element.
3. The algorithm then recursively sorts the two sublists using the same process
   until the sublists are fully sorted.
4. Finally, the algorithm merges the sorted sublists back together to form
   the final sorted list.
"""

from copy import copy


def quick_sort(array, left=None, right=None):
    """Returns sorted array, using the `Quick Sort` algorithm."""
    if not left and not right:
        left, right = 0, len(array) - 1

    if left < right:  # type: ignore
        pivot = left
        for i in range(left + 1, right + 1):  # type: ignore
            # Check if the element is smaller than the pivot element.
            if array[i] < array[left]:
                pivot += 1  # type: ignore
                value = array[pivot]
                array[pivot] = array[i]
                array[i] = value
        value = array[left]
        array[left] = array[pivot]
        array[pivot] = value

        quick_sort(array, left, pivot - 1)  # type: ignore
        quick_sort(array, pivot + 1, right)  # type: ignore

    return array


l1 = [1, 5, 2, 2, 4, 6, 7, 12, 32, 5, 1, 35, 6]
l1_sorted = quick_sort(copy(l1))

assert l1 == [1, 5, 2, 2, 4, 6, 7, 12, 32, 5, 1, 35, 6]
assert l1_sorted == [1, 1, 2, 2, 4, 5, 5, 6, 6, 7, 12, 32, 35]
