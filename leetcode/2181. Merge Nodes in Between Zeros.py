class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head.next
        summ = 0
        dummy = ListNode(0)
        tail = dummy
        while curr is not None:
            if curr.val > 0:
                summ += curr.val
            if curr.val == 0 and summ > 0:
                tail.next = ListNode(summ)
                tail = tail.next
                summ = 0
            curr = curr.next
        return dummy.next
