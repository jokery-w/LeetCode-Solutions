class Solution(object):
    def maximumWealth(self, accounts):
        return max(sum(customer) for customer in accounts)
