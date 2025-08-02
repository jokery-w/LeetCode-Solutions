class Solution(object):
    def getConcatenation(self, nums):
        ans = ([0] * 2) * len(nums)
        for i in range(2*len(nums)):
            ans = nums * 2
        return ans