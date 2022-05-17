# https://leetcode.com/problems/odd-even-linked-list
# https://sanghoonly.tistory.com/16?category=990444


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 본 코드는 odd 노드와 even 노드를 구분하지 않고 구현한 코드.
def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    even_head, cur, prev = head.next, head, None
    length = 1

    while cur and cur.next:
        prev = cur
        next = cur.next
        cur.next = cur.next.next
        cur = next
        length += 1

    if length % 2:
        cur.next = even_head
    else:
        prev.next = even_head

    return head
