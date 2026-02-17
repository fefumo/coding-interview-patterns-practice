""" 
Invert a binary tree and return its root. When a binary tree is inverted, it becomes the
mirror image of itself.
"""

from tree_template import *


def invert(root: TreeNode | None):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)
    return root


def invert_iterative(root: TreeNode | None):
    if not root:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root


def main():
    t = build_height_3_tree()
    print_tree(t)

    print('-'*20)

    inverted = invert(t)
    print_tree(inverted)


if __name__ == "__main__":
    main()
