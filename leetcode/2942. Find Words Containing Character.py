class Solution(object):
    def findWordsContaining(self, words, x):
        return [_ for _, val in enumerate(words) if x in val]