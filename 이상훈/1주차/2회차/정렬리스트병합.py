# https://leetcode.com/problems/merge-two-sorted-lists/submissions/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists( list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    ptr = head

    while list1 and list2:
        if list1.val < list2.val:
            head.next = list1
            list1 = list1.next
        else:
            head.next = list2
            list2 = list2.next

        head = head.next

    if not list1:
        head.next = list2
    else:
        head.next = list1

    return ptr.next
