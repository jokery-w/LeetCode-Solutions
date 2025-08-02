
class Solution(object):
    def numIdenticalPairs(self, nums):
        freq = build_counter(nums)
        count = 0
        for f in freq.values():
            count += f * (f - 1) // 2
        return count


def build_counter(data):
        counter = {}
        for item in data:
            if item in counter:
                counter[item] += 1
            else:
                counter[item] = 1
        return counter