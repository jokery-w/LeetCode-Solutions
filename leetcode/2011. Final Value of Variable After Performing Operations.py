class Solution(object):
    def finalValueAfterOperations(self, operations):
        count = 0
        for i in range(len(operations)):
            if "++" in operations[i]:
                count += 1
            else:
                count -= 1
        return count