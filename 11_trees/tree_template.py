from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


def build_height_3_tree():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)

    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)

    return root


def build_height_4_tree():
    root = TreeNode(10)

    root.left = TreeNode(5)
    root.right = TreeNode(15)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)

    root.left.left.left = TreeNode(1)
    root.left.left.right = TreeNode(4)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(8)

    root.right.left.left = TreeNode(11)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(16)
    root.right.right.right = TreeNode(20)

    return root


def print_tree(root):
    def _rec(node, prefix="", is_left=True):
        if not node:
            return
        if node.right:
            _rec(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        if node.left:
            _rec(node.left, prefix + ("    " if is_left else "│   "), True)

    if root is None:
        print("<empty tree>")
    else:
        _rec(root)
