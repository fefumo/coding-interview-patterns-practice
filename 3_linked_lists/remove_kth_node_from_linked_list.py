""" 
Return the head of a singly linked list
after removing the k'th node from the end of it.
"""


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def remove_kth_node_basic(head: ListNode, k: int):
    nodes_amount: int = 0
    dummy = head
    # traverse to find out the size of the list
    while dummy:
        nodes_amount += 1
        dummy = dummy.next
    node_before_target = nodes_amount - k - 1

    if node_before_target < 0:  # then we have to return list without the 1st node
        return head.next

    dummy = head  # reset dummy
    # place the head before the target node
    for _ in range(node_before_target):
        head = head.next
    head.next = head.next.next
    return dummy


def remove_kth_node_optimised(head: ListNode, k: int):
    """ Use two pointers to traverse the list only once """
    dummy = ListNode(-1, head)  # create dummy in case the head is the node we want to remove
    trailer = leader = dummy

    # advance leader k nodes ahead
    for _ in range(k):
        leader = leader.next
        # if k is larger than the size of linked list, dont do anything
        if not leader:
            return head

    # move leader to the end of the list, keeping
    # trailer k nodes behind
    while leader.next:
        trailer = trailer.next
        leader = leader.next

    # remove kth node from the end
    trailer.next = trailer.next.next
    return dummy.next


def traverse_list(node: ListNode):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


def main():
    node6 = ListNode(6, None)
    node5 = ListNode(5, node6)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    traverse_list(node1)
    result = remove_kth_node_basic(node1, 1)
    traverse_list(result)


if __name__ == "__main__":
    main()
