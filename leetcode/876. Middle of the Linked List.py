# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        if head is None:
            return head
        curr = head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next

        for _ in range(count // 2):
            head = head.next

        return head