"""
Given a singly linked list, determine if it contains a cycle. A cycle occurs if a node's next
pointer references an earlier node in the list, causing a loop.
"""


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def linked_list_loop_naive(head: ListNode) -> bool:
    visited = set()
    curr = head
    while curr:
        if curr in visited:
            return True
        curr = curr.next
    return False


def floyd_cycle_detection(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False
