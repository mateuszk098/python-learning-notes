"""
Linked List naive test.
"""

from my_types import doubly_linked_list as dll


def main():

    l1 = dll.DoublyLinkedList()
    for number in range(5):
        l1.add_last(number)

    print(">>> l1.print_forward()")
    l1.print_forward()

    print("\n>>> l1.print_backward()")
    l1.print_backward()

    print("\n>>> l1.length")
    print(l1.length)

    print("\n>>> l1.add_last(5)")
    l1.add_last(5)
    l1.print_forward()

    print("\n>>> l1.add_first(-1)")
    l1.add_first(-1)
    l1.print_forward()

    print("\n>>> l1.add_at(10, 3)")
    l1.add_at(10, 3)
    l1.print_forward()

    print("\n>>> l1.length")
    print(l1.length)

    print("\n>>> l1.remove_last()")
    l1.remove_last()
    l1.print_forward()

    print("\n>>> l1.remove_first()")
    l1.remove_first()
    l1.print_forward()
    print(l1.length)

    print("\n>>> l1.remove_at(5)")
    l1.remove_at(5)
    l1.print_forward()

    print("\n>>> l1.length")
    print(l1.length)

    print("\n>>> l1.get_at(2)")
    print(l1.get_at(2))

    print("\n>>> l1.reverse()")
    l1.reverse()
    l1.print_forward()

    print("\n>>> l1.print_backward()")
    l1.print_backward()

    print("\n>>> l1.exist(10)")
    print(l1.exist(10))

    print("\n>>> l1.remove_value(2)")
    l1.remove_value(2)
    l1.print_forward()

    l2 = dll.DoublyLinkedList()

    print("\n>>> l2.add_with_sort()")
    for number in [5, 1, 3, 2, -1, 0]:
        l2.add_with_sort(number)
    l2.print_forward()

    print("\n>>> l2.reverse()")
    l2.reverse()
    l2.print_forward()

    print("\n>>> l2.print_backward()")
    l2.print_backward()


if __name__ == "__main__":
    main()
