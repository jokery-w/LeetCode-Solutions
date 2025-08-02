class Solution(object):
    def validStrings(self, n):
        res = [""]
        for _ in range(n):
            temp = []
            for s in res:
                for bit in ['0', '1']:
                    if bit == '0' and s[-1:] == "0":
                        continue
                    temp.append(s + bit)
            res = temp
        return res