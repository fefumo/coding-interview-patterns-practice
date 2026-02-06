""" 
Return the node where two singly linked lists intersect.
If the lists don't intersect, return null.
"""


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def naive_approach(head1: ListNode, head2: ListNode):
    '''
    takes O(n) space. 

    traverse the first linked list  once and store each
    node in a hash set. Next, we traverse the second linked
    list until we  find the first node that exists
    in the hash set, signifying the intersection point since it's
    the first node shared between the two linked lists.
    '''

    hash_table = {}
    dummy = head1
    while dummy:
        hash_table[dummy] = dummy.val
        dummy = dummy.next
    dummy = head2
    while dummy:
        if dummy in hash_table:
            return dummy
        hash_table[dummy] = dummy.val
        dummy = dummy.next

    return None


def intersection_optimised(head1: ListNode, head2: ListNode):
    '''
    Traverse the lists from both ends. If the pointers are pointing
    at the same object at the same time, then we've found an intersection.
    '''
    p1 = head1
    p2 = head2
    while p1 != p2:
        if p1:
            p1 = p1.next
        else:
            p1 = head2

        if p2:
            p2 = p2.next
        else:
            p2 = head1
        # at this point, both pointers are either null or pointing at the same node

    return p1


def print_table(ht):
    for item in ht:
        print(item.val)


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

    second_head3 = ListNode(9, node1)
    second_head2 = ListNode(8, second_head3)
    second_head1 = ListNode(7, second_head2)

    no_intersection_head2 = ListNode(11, None)
    no_intersection_head = ListNode(10, no_intersection_head2)

    result = naive_approach(node1, second_head1)
    result2 = naive_approach(node1, no_intersection_head)
    opt_result = intersection_optimised(node1, second_head1)
    opt_result2 = intersection_optimised(node1, no_intersection_head)

    if result:
        print(result.val)
    else:
        print("no intersection")

    if result2:
        print(result2.val)
    else:
        print("no intersection")

    if opt_result:
        print(opt_result.val)
    else:
        print("no_intersection")

    if opt_result2:
        print(opt_result2.val)
    else:
        print("no_intersection")


if __name__ == "__main__":
    main()
