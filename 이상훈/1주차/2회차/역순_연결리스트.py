from typing import Optional


class ListNode:
    pass


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    last_node = reverseList(head.next)
    head.next.next = head
    head.next = None


    return last_node

