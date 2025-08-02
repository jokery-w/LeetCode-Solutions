class Solution(object):
    def minOperations(self, boxes):
        res = []
        for i in range(len(boxes)):
            c = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    c += abs(i - j)

            res.append(c)

        return res