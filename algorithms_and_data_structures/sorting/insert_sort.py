"""
Example implementation of the Insert Sort O(N^2).
"""


def insert_sort(array):
    """Returns sorted array, using the insert sort algorithm."""
    length = len(array)
    if length <= 1:
        return
    for i in range(1, length):
        j = i  # 0, ..., i-1 elements are sorted.
        value = array[j]
        while j > 0 and array[j-1] > value:
            array[j] = array[j-1]
            j -= 1
        array[j] = value


l = [1, 5, 2, 2, 4, 6, 7, 12, 32, 5, 1, 35, 6]
insert_sort(l)
print(l)
