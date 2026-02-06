""" 
Reverse a singly-linked list
"""


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def reverse_linked_list(node: ListNode):
    prev_node = None
    cur_node = node
    while cur_node:
        next_node = cur_node.next
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = next_node

    return prev_node  # will point at the first element of the reversed linked list


def reversal_recursive(head: ListNode):
    # i still dont understand how it works...
    if not head or not head.next:
        return head
    new_head = reversal_recursive(head.next)
    print(
        f'this is the first head that was found after recursion {new_head.val}')
    head.next.next = head
    head.next = None
    return new_head


def traverse_list(node: ListNode):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


def main():
    node3 = ListNode(3, None)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    # traverse_list(node1)
    # new_first_node = reverse_linked_list(node1)
    # if new_first_node:
    #     # traverse_list(new_first_node)
    #     reversal_recursive(new_first_node)
    reversal_recursive(node1)


if __name__ == "__main__":
    main()
