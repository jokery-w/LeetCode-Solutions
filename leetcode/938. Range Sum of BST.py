# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root is None:
            return 0
        q = [root]
        tol = 0
        while q:
            curr = q.pop(0)
            if curr is None:
                continue

            if low <= curr.val <= high:
                tol += curr.val

            if curr.val > low:
                q.append(curr.left)

            if curr.val < high:
                q.append(curr.right)

        return tol
