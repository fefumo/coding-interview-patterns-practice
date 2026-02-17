""" 
Return the maximum sum of a continuous path in a binary tree. A path is defined by the
following characteristics:
    • Consists of a sequence of nodes that can begin and end at any node in the tree
    • Each consecutive pair of nodes in the sequence is connected by an edge
    • The path must be a single continuous sequence of nodes that doesn't split into multiple paths
"""

from tree_template import *

max_sum = float('-inf')


def max_path_sum(root):
    global max_sum
    max_path_sum_helper(root)
    return max_sum


def max_path_sum_helper(node):
    global max_sum
    if not node:
        return 0

    left_sum = max(max_path_sum_helper(node.left), 0)
    right_sum = max(max_path_sum_helper(node.right), 0)
    max_sum = max(max_sum, node.val + left_sum + right_sum)

    return node.val + max(left_sum, right_sum)


def main():
    root = TreeNode(5)

    root.left = TreeNode(-10)
    root.right = TreeNode(8)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(-7)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(7)

    root.left.left.left = TreeNode(11)
    root.left.right.right = TreeNode(-1)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(-3)
    print_tree(root)
    print(max_path_sum(root))


if __name__ == "__main__":
    main()
