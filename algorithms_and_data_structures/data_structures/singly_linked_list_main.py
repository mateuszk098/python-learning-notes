"""
Linked List naive test.
"""

from my_types import singly_linked_list as sll


def main():

    l1 = sll.SinglyLinkedList()
    for number in range(5):
        l1.add_last(number)

    print(">>> l1.print_out()")
    l1.print_out()

    print("\n>>> l1.length")
    print(l1.length)

    print("\n>>> l1.add_last(5)")
    l1.add_last(5)
    l1.print_out()

    print("\n>>> l1.add_first(-1)")
    l1.add_first(-1)
    l1.print_out()

    print("\n>>> l1.add_at(10, 3)")
    l1.add_at(10, 3)
    l1.print_out()

    print("\n>>> l1.length")
    print(l1.length)

    print("\n>>> l1.remove_last()")
    l1.remove_last()
    l1.print_out()

    print("\n>>> l1.remove_first()")
    l1.remove_first()
    l1.print_out()

    print("\n>>> l1.remove_at(4)")
    l1.remove_at(4)
    l1.print_out()

    print("\n>>> l1.length")
    print(l1.length)

    print("\n>>> l1.get_at(2)")
    print(l1.get_at(4))

    print("\n>>> l1.reverse()")
    l1.reverse()
    l1.print_out()

    print("\n>>> l1.exist(10)")
    print(l1.exist(10))

    print("\n>>> l1.remove_value(2)")
    l1.remove_value(2)
    l1.print_out()

    l2 = sll.SinglyLinkedList()
    for number in [1, 5, 3, 2, 4]:
        l2.add_with_sort(number)

    l3 = sll.SinglyLinkedList()
    for number in range(5):
        l3.add_last(number)

    print("\n>>> l2.add_with_sort()")
    l2.print_out()

    print("\n>>> l3.add_last()")
    l3.print_out()

    print("\n>>> ll.safe_concat(l2, l3)")
    l4 = sll.safe_concat(l2, l3)
    l4.print_out()
    print("Not Modified l2")
    l2.print_out()
    print("Not modified l3")
    l3.print_out()

    print("\n>>> ll.fast_concat(l2, l3)")
    l4 = sll.fast_concat(l2, l3)
    l4.print_out()
    print("Modified l2")
    l2.print_out()
    print("Not modified l3")
    l3.print_out()

    l5 = sll.SinglyLinkedList()
    for number in [1, 5, 3, 2, 4]:
        l5.add_with_sort(number)

    l6 = sll.SinglyLinkedList()
    for number in range(5):
        l6.add_last(number)

    print("\n>>> l5.add_with_sort()")
    l5.print_out()

    print("\n>>> l6.add_last()")
    l6.print_out()

    print("\n>>> ll.concat_and_sort(l5, l6)")
    l7 = sll.concat_and_sort(l5, l6)
    l7.print_out()
    print("Modified l5")
    l5.print_out()
    print("Modified l6")
    l6.print_out()


if __name__ == "__main__":
    main()
