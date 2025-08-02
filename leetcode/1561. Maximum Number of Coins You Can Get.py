class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        l = []
        for i in range(len(piles)):
            l.append(piles[i])
        a = 0
        while l:
            l.pop()
            a += l.pop()
            l.pop(0)
        return a