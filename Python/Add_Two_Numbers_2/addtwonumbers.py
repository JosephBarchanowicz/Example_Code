class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        cur = head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            val = l1val + l2val + carry
            carry = val // 10
            new_node = ListNode(val % 10)
            if head is None:
                cur = new_node
                head = cur
            else:
                cur.next = new_node
                cur = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head






