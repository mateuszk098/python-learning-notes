"""
Binary Search Tree naive test.
"""

from my_types import binary_search_tree as bst


def main():

    b = bst.BinarySearchTree()
    keys = [19, 4, 3, 12, 8, 14, 25, 27, 26, 31]
    values = [19, 4, 3, 12, 8, 14, 25, 27, 26, 31]
    for key, value in zip(keys, values):
        b.push(key, value)

    print("b.search(19) node value")
    node1 = b.search(19)
    print(node1.value)  # type: ignore

    print("\nb.get_min()")
    node2 = b.get_min()
    print("Key", node2.key, "Value", node2.value)  # type: ignore

    print("\nb.get_max()")
    node3 = b.get_max()
    print("Key", node3.key, "Value", node3.value)  # type: ignore

    print("\nPre-Order")
    b.pre_order(b.root)
    print("\n\nIn-Order")
    b.in_order(b.root)
    print("\n\nPost-Order")
    b.post_order(b.root)

    print("\n\nPre-Order")
    bst.remove_node(b.root, 12)
    b.pre_order(b.root)


if __name__ == "__main__":
    main()
