""" 
Return the width of the widest level in a binary tree, where the width of a level is defined
as the distance between its leftmost and rightmost non-null nodes.
"""

from collections import deque
from tree_template import *


def calc_widest_level(root):
    if not root:
        return 0

    max_width = 0
    queue = deque([(root, 0)])

    while queue:
        level_size = len(queue)
        leftmost = queue[0][1]  # the index of the first node of this level
        rightmost = leftmost
        for _ in range(level_size):
            node, i = queue.popleft()
            if node.left:
                queue.append((node.left, 2*i + 1))
            if node.right:
                queue.append((node.right, 2*i + 2))
            rightmost = i
        max_width = max(max_width, rightmost - leftmost + 1)

    return max_width


def main():
    root = build_height_4_tree()
    root.left.left.right = None
    root.right.right = None
    root.right.left.left = None
    print_tree(root)
    res = calc_widest_level(root)
    print(res)


if __name__ == "__main__":
    main()
