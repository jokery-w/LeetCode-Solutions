# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def searchBST(self, root, val):
        if root is None:
            return root

        q = [root]
        while q:
            p = q.pop(0)

            if p.val == val:
                return p

            if val < p.val:
                q.append(p.left)
            else:
                q.append(p.right)
