"""
Iterable List naive test.
"""

from my_types import iterable_list as il


def main():

    l1 = il.IterableList()
    l1.add_last(0)
    l1.add_last(1)
    l1.add_last(2)
    l1.add_last(3)
    l1.print_out()

    # Biggest advantage - traversing with loop.
    for value in l1:
        print(value, end=" ")


if __name__ == "__main__":
    main()
