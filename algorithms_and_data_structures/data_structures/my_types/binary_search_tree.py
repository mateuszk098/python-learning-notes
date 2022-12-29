"""
Example implementation of the Binary Search Tree.

A binary search tree (BST) is a data structure that allows efficient insertion,
deletion, and search operations. It is called a "search tree" because it can be
used to search for specific values in the tree.

Advantages of binary search trees include:

* Efficiency: BSTs have an average-case time complexity of O(log n) for search,
  insert, and delete operations, making them efficient for large datasets.

* Sorted data: BSTs store data in a sorted manner, which can be useful in certain
  applications.

* Flexibility: BSTs can be easily modified to store additional data or to support
  different operations.

Some disadvantages of BSTs include:

* Unbalanced trees: If a BST becomes unbalanced (i.e., if the left and right subtrees
  are significantly different in size), the time complexity of the search, insert,
  and delete operations can degrade to O(n).

* Limited range of operations: BSTs are not well-suited for operations that require
  finding the minimum or maximum value in the tree, as these operations require
  traversing the entire tree.

BSTs are a good choice for applications that require efficient search, insert, and delete
operations on a dataset that does not change frequently and does not require support for
minimum/maximum operations. They are commonly used in database indexing, search engines,
and other applications where fast access to data is important.
"""


class Node:
    """Provides a single node of the binary search tree."""

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Provides an example of a binary search tree."""

    def __init__(self):
        self.root = None

    def search(self, key):
        """Returns node for which `key` attribute is equal
        to `key` argument. If such a node does not exist, returns None."""
        if self.root is None:
            return None
        node = self.root
        while node.key != key and node is not None:  # type: ignore
            if key < node.key:  # Go to the left.
                node = node.left
            else:
                node = node.right
        return node

    def push(self, key, value):
        """Push a new node to the tree."""
        new_node = Node(key, value)
        if self.root is None:
            self.root = new_node
            return
        node = self.root
        while True:
            parent = node
            if key < node.key:  # Go to the left.
                node = node.left
                if node is None:  # End of the path, push as the left child.
                    parent.left = new_node  # type: ignore
                    break
            else:  # Go to the right.
                node = node.right
                if node is None:  # End of the path, push as the right child.
                    parent.right = new_node  # type: ignore
                    break

    def get_min(self):
        """Returns node with the minimal key."""
        node = self.root
        while node.left is not None:  # type: ignore
            node = node.left  # type: ignore
        return node

    def get_max(self):
        """Returns node with the maximal key."""
        node = self.root
        while node.right is not None:  # type: ignore
            node = node.right  # type: ignore
        return node

    def pre_order(self, node):
        """Tranverse the tree along pre-order path.
        The root first, next left and right subtree."""
        if node is not None:
            print(node.key, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        """Tranverse the tree along in-order path. The left subtree
        first, next the node, and next the right subtree."""
        if node is not None:
            self.in_order(node.left)
            print(node.key, end=" ")
            self.in_order(node.right)

    def post_order(self, node):
        """Tranverse the tree along in-order path. The left subtree
        first, next the right subtree, and next the node."""
        if node is not None:
            self.in_order(node.left)
            self.in_order(node.right)
            print(node.key, end=" ")


def remove_node(node, key_to_remove):
    """Remove the node with `key_to_remove`. The `node` is the node we start from."""
    if node is None:
        return node
    if key_to_remove < node.key:  # Go to the left.
        node.left = remove_node(node.left, key_to_remove)
    elif key_to_remove > node.key:  # Go to the right.
        node.right = remove_node(node.right, key_to_remove)
    else:  # Remove found node.
        # Only one child.
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        # Two childs.
        tmp = _get_min(node.right)
        node.key = tmp.key
        node.right = remove_node(node.right, tmp.key)
    return node


def _get_min(node):
    """Only for internal use. Return node with the minimal key
    in the tree or the subtree, depending on the given `node`."""
    tmp_node = node
    while tmp_node.left is not None:
        tmp_node = tmp_node.left
    return tmp_node
