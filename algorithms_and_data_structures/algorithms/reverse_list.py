"""
Write an algorithm which reverses the given list of integers.
Write recursive and iterative versions.
"""


def reverse_rec(lst, left, right):
    """Recursive version of list reversion."""
    if left < right:
        lst[left], lst[right] = lst[right], lst[left]
        return reverse_rec(lst, left + 1, right - 1)


def reverse_iter(lst):
    """Iterative version of list reversion."""
    left = 0
    right = len(lst) - 1

    for i in range(len(lst) // 2):
        lst[left+i], lst[right-i] = lst[right-i], lst[left+i]


my_lst1 = [4, 5, 6, 7, 8, 9]
print("Recursive")
print(my_lst1)
reverse_rec(my_lst1, 0, len(my_lst1) - 1)
print(my_lst1)

print("\nIterative")
my_lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_lst2)
reverse_iter(my_lst2)
print(my_lst2)
