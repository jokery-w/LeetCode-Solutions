class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0
        s = set(allowed)
        for i in range(len(words)):
            if all(char in s for char in words[i]):
                count +=1
        return count