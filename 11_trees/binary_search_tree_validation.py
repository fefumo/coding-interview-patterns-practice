""" 
Verify whether a binary tree is a valid binary search tree (BST). A BST is a binary tree where
each node meets the following criteria:
    • A node's left subtree contains only nodes of lower values than the node's value.
    • A node's right subtree contains only nodes of greater values than the node's value.
"""

from tree_template import *


def validate_binary_tree(root):
    lower_bound = float('-inf')
    upper_bound = float('inf')
    return is_within_bounds(root, lower_bound, upper_bound)


def is_within_bounds(node, lower_bound, upper_bound):
    if not node:
        return True
    if not lower_bound < node.val < upper_bound:
        return False
    if not is_within_bounds(node.left, lower_bound, node.val):
        return False
    return is_within_bounds(node.right, node.val, upper_bound)


def main():
    # too lazy...
    pass


if __name__ == "__main__":
    main()
