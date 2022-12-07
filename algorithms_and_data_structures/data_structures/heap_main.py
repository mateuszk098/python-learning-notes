"""
Heap naive test.
"""

from my_types import heap as hp


def main():

    h = hp.Heap(6)
    for element in [54, 24, 5, 47, 13, 58]:
        h.push(element)
    h.print()

    element = h.pop()
    print("Pop:", element)
    h.print()

    # Sorting with heap structure - O(2nlogn), while QuickSort has O(nlogn).
    l = [1, 48, 24, 9, 3, 65, 28, 13]
    heap = hp.Heap(len(l))
    for element in l:
        heap.push(element)  # O(logn)
    for index in range(len(l) - 1, -1, -1):
        l[index] = heap.pop()  # O(logn)
    print(l)


if __name__ == "__main__":
    main()
