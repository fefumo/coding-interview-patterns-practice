""" 
Given a singly linked list, find and return its middle node.
If there are two middle nodes, return the second one.

Constraints:
• The linked list contains at least one node.
• The linked list contains unique values.
"""


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def linked_list_midpoint(head: ListNode):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def main():
    node7 = ListNode(7, None)
    node6 = ListNode(6, node7)
    node5 = ListNode(5, node6)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    res = linked_list_midpoint(node1)
    print(res.val)


if __name__ == "__main__":
    main()
