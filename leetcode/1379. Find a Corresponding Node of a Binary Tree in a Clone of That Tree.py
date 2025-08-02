# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        if original and cloned is None:
            return None


        q = [original]
        qq = [cloned]
        while q and qq:
            curr = q.pop(0)
            cuur = qq.pop(0)
            if curr is target:
                return cuur
            if curr is None:
                continue

            q.append(curr.left)
            qq.append(cuur.left)

            q.append(curr.right)
            qq.append(cuur.right)
