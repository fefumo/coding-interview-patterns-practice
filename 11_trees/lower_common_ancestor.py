""" 
Return the lowest common ancestor (LCA) of two nodes, p and q, in a binary tree. The
LCA is defined as the lowest node that has both p and q as descendants. A node can be
considered an ancestor of itself.

Constraints:
    • The tree contains at least two nodes.
    • All node values are unique.
    • p and q represent different nodes in the tree.
"""

from tree_template import *

# It could be cleaner, but its my own solution
# which I'm proud of :3
# tested on LeetCode and it works!
def solve(root, p, q):
    node = root
    return find_lca(node, p, q)


def find_lca(node, p, q):

    if not node:
        return None
    if p < node.val and q < node.val:
        return find_lca(node.left, p, q)
    if p > node.val and q > node.val:
        return find_lca(node.right, p, q)
    if p < node.val and q > node.val:
        return node
    return node


def main():
    #tree...

    print_tree(root)
    p, q = 5,4
    res = solve(root, p, q)
    print(res.val)


if __name__ == "__main__":
    main()
