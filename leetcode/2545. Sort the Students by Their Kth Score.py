class Solution(object):
    def sortTheStudents(self, score, k):
        return sorted(score, reverse=True, key=lambda row:row[k])