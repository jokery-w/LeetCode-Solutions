# Definition for singly-linked list.
import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        while curr.next is not None:
            sub = math.gcd(curr.val, curr.next.val)
            new = ListNode(sub)
            n_node = curr.next
            curr.next = new
            new.next = n_node
            curr = n_node
        return head