class Solution(object):
    def maximumCount(self, nums):
        count = 0
        neg_count = 0
        for i in range(len(nums)):
            if nums[i] >= 1:
                count += 1
            elif nums[i] == 0:
                continue
            else:
                neg_count += 1
        return max(count, neg_count)