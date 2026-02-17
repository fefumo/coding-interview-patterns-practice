""" 
Determine if a binary tree is height-balanced, meaning no node's left subtree and right
subtree have a height difference greater than 1.
"""

from tree_template import *


def get_height_imbalance(node: TreeNode | None):
    if not node:
        return 0
    left_height = get_height_imbalance(node.left)
    right_height = get_height_imbalance(node.right)

    if left_height == -1 or right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1

    return 1 + max(left_height, right_height)


def balanced_binary_tree_validation(root: TreeNode):
    if get_height_imbalance(root) == -1:
        return False
    else:
        return True


def main():
    t = build_height_4_tree()
    print_tree(t)
    print(balanced_binary_tree_validation(t))
    print(f'with only one node added: {balanced_binary_tree_validation(t)}')
    print('-'*40)

    t.left.left.left.left = TreeNode(99)
    t.left.left.left.left.left = TreeNode(100)
    print_tree(t)
    print(balanced_binary_tree_validation(t))


if __name__ == "__main__":
    main()
