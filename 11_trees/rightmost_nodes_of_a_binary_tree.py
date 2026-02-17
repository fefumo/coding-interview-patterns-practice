""" 
Return an array containing the values of the rightmost nodes at each level of a binary tree.
"""

from collections import deque
from tree_template import *


def solve(root):
    queue = deque([root])
    res = []
    # for the current level: for each node, pop it from the queue
    # and add its children to the queue
    while queue:
        if not root:
            return []
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # in the book there was a check 'if i == level_size - 1'
        # but i havent found the reason to do that cuz i should be
        # pointing to the rightmost node after the loop
        # but maybe i am just dumb...
        res.append(node.val)
    return res


def main():
    t = build_height_4_tree()
    t.right.right = None
    t.right.left.right = None
    t.right.left.left = None
    print_tree(t)
    print(solve(t))


if __name__ == "__main__":
    main()
