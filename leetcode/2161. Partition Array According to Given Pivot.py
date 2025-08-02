class Solution(object):
    def pivotArray(self, nums, pivot):
        res1 = []
        res2 = []
        res3 = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                res1.append(nums[i])
            elif nums[i] == pivot:
                res2.append(nums[i])
            else:
                res3.append(nums[i])
        return (res1 + res2 + res3)