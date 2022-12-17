"""
Example implementation of the Quicksort O(NlogN).
"""


def quick_sort(array, left, right):
    """Returns sorted array, using the quick sort algorithm."""
    if left < right:
        pivot = left
        for i in range(left+1, right+1):
            if array[i] < array[left]:
                pivot += 1
                value = array[pivot]
                array[pivot] = array[i]
                array[i] = value
        value = array[left]
        array[left] = array[pivot]
        array[pivot] = value

        quick_sort(array, left, pivot-1)
        quick_sort(array, pivot+1, right)


l = [1, 5, 2, 2, 4, 6, 7, 12, 32, 5, 1, 35, 6]
quick_sort(l, 0, len(l)-1)
print(l)
