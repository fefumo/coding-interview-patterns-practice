""" 
Construct a binary tree using arrays of values obtained after a preorder traversal and an
inorder traversal of the tree
"""

from tree_template import *


inorder_indexes_map = {}
preorder_index = 0


def build_tree(preorder, inorder):
    global inorder_indexes_map
    for i, val in enumerate(inorder):
        inorder_indexes_map[val] = i
    return build_subtree(0, len(inorder) - 1, preorder, inorder)


def build_subtree(left, right, preorder, inorder):
    global preorder_index, inorder_indexes_map
    if left > right:
        return None
    val = preorder[preorder_index]
    inorder_index = inorder_indexes_map[val]
    node = TreeNode(val)
    preorder_index += 1
    node.left = build_subtree(left, inorder_index - 1, preorder, inorder)
    node.right = build_subtree(inorder_index + 1, right, preorder, inorder)
    return node


def main():
    # honestly, i cheesed this problem. i am weak.
    pass


if __name__ == "__main__":
    main()
