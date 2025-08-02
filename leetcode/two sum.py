class Solution(object):
    def twoSum(self, nums, target):
        pair = {}
        for i, num in enumerate(nums):
            come = target - num
            if come in pair:
                return[pair[come], i]
            pair[num] = i
        return pair
