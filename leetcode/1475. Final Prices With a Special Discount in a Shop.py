class Solution(object):
    def finalPrices(self, prices):
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i and prices[i] >= prices[j]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices