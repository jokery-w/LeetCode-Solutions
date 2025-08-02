# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def getDecimalValue(self, head):
        if head is None:
            return
        pos = 0
        curr = head
        while curr is not None:
            pos = pos * 2 + curr.val
            curr = curr.next
        return pos
