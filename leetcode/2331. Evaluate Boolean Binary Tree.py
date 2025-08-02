# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def evaluateTree(self, root):
        if root is None:
            return False

        if root.left:
            l_root = self.evaluateTree(root.left)

        if root.right:
            r_root = self.evaluateTree(root.right)

        if root.val == 2:
            return l_root or r_root
        if root.val == 3:
            return l_root and r_root

        if root.left is None and root.right is None:
            return True if root.val == 1 else False