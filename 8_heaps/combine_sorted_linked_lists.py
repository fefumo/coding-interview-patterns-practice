""" 
Given k singly linked lists, each sorted in ascending order, combine them into one sorted
linked list.
"""

from __future__ import annotations
import heapq


class ListNode:
    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


def combine_sorted_lists(l: list[ListNode]) -> ListNode:
    heap = []
    for node in l:
        if node:
            heapq.heappush(heap, node)

    # kinda dummy node. advance it once to get the final result
    res_head = ListNode(0, None)
    dummy = res_head

    while heap:
        cur_head = heapq.heappop(heap)
        res_head.next = cur_head
        if cur_head.next:
            heapq.heappush(heap, cur_head.next)
        res_head = res_head.next

    assert dummy.next is not None
    return dummy.next


def traverse_list(head: ListNode | None):
    while head:
        print(head.val)
        head = head.next


def main():
    first_list2 = ListNode(6, None)
    first_list_head = ListNode(1, first_list2)

    second_list3 = ListNode(6, None)
    second_list2 = ListNode(4, second_list3)
    second_list_head = ListNode(1, second_list2)

    third_list2 = ListNode(7, None)
    third_list_head = ListNode(3, third_list2)

    lists = [first_list_head, second_list_head, third_list_head]

    result = combine_sorted_lists(lists)
    traverse_list(result)


if __name__ == "__main__":
    main()
