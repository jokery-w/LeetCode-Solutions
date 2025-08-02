class Solution(object):
    def targetIndices(self, nums, target):
        tol = []
        n = sorted(nums)
        for i in range(len(nums)):
            if n[i] == target:
                tol.append(i)
        return tol
