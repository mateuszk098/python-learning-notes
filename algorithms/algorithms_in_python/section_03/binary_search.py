"""
Write an algorithm which realises binary search on a given integers list.
The binary search algorithm assumes the list is sorted!
Write recursive and iterative versions. 

Description: https://en.wikipedia.org/wiki/Binary_search_algorithm
"""


def binary_search_rec(lst, number, left, right):
    """Recursive version of binary search."""
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if lst[mid] == number:
        return mid
    elif number < lst[mid]:
        return binary_search_rec(lst, number, left, mid - 1)
    elif number > lst[mid]:
        return binary_search_rec(lst, number, mid + 1, right)


def binary_search_iter(lst, number):
    """Iterative version of binary search."""
    if not lst:
        return -1

    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if lst[mid] == number:
            return mid
        elif number < lst[mid]:
            end = mid - 1
        elif number > lst[mid]:
            start = mid + 1

    return -1


my_lst = [1, 2, 6, 9, 18, 21]
number = 21
index1 = binary_search_rec(my_lst, number, 0, len(my_lst) - 1)
index2 = binary_search_iter(my_lst, number)

print(f"Recursion: {index1}")
print(f"Iteration: {index2}")
