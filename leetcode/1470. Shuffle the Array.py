class Solution(object):
    def shuffle(self, nums, n):
        arr = []
        for x in range(len(nums) - n):
            arr.append(nums[x])
            arr.append(nums[x + n])

        return arr