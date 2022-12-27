"""
Example implementation of the Merge Sort.

Merge Sort algorithm is a sorting algorithm that works by dividing an array
into two parts, sorting each part, and then merging the sorted parts back together.

Time complexity: O(n*log(n))
Space complexity: O(n)

"""

from copy import copy


def merge_sort(array, left=0, right=None):
    """Returns sorted array, using the `Merge Sort` algorithm."""
    if right is None:
        right = len(array) - 1

    if left < right:
        mid = left + (right - left) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        _merge(array, left, mid, right)

    return array


def _merge(array, left, mid, right):
    """Merges two sorted sub-arrays into a single sorted array."""
    left1, right1 = left, mid
    left2, right2 = mid + 1, right
    temp = []  # Create a temporary array to store the merged elements.

    # Merge the two sub-arrays.
    while left1 <= right1 and left2 <= right2:
        if array[left1] < array[left2]:
            temp.append(array[left1])
            left1 += 1
        else:
            temp.append(array[left2])
            left2 += 1

    # Add any remaining elements from the first sub-array
    while left1 <= right1:
        temp.append(array[left1])
        left1 += 1

    # Add any remaining elements from the second sub-array
    while left2 <= right2:
        temp.append(array[left2])
        left2 += 1

    # Copy the sorted elements back into the original array
    for i in range(left, right + 1):
        array[i] = temp[i - left]


l1 = [1, 5, 2, 2, 4, 6, 7, 12, 32, 5, 1, 35, 6]
l1_sorted = merge_sort(copy(l1))

assert l1 == [1, 5, 2, 2, 4, 6, 7, 12, 32, 5, 1, 35, 6]
assert l1_sorted == [1, 1, 2, 2, 4, 5, 5, 6, 6, 7, 12, 32, 35]
