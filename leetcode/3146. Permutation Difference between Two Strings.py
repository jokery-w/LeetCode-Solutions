class Solution(object):
    def findPermutationDifference(self, s, t):
        res = 0
        m = {}
        for i in range(len(s)):
            m[t[i]] = i
        for i in range(len(s)):
            res += abs(i - m[s[i]])
        return res