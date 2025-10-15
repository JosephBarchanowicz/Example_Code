# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        cur = head
        cur_next = cur.next
        while cur != cur_next:
            if cur_next is None or cur_next.next is None:
                return False
            cur = cur.next
            cur_next = cur_next.next.next
        return True



