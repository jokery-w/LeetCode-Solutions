class Solution(object):
    def minimumOperations(self, nums):
        x = 0
        for i in range(len(nums)):
            if nums[i] % 3 != 0:
               x += min(nums[i] % 3, 3 - (nums[i] % 3))
            else:
                x += min(nums[i] % 3, 3 + (nums[i] % 3))
        return x
