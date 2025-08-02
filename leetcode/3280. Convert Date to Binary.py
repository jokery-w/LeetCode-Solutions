class Solution(object):
    def convertDateToBinary(self, date):
        parts = date.split("-")
        y = bin(int(parts[0]))[2:]
        m = bin(int(parts[1]))[2:]
        d = bin(int(parts[2]))[2:]
        return y + "-" + m + "-" + d
