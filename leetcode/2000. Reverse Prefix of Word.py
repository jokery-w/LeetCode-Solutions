class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        st = list(word)
        count = 0
        for i in range(len(word)):
            count += 1
            if word[i] == ch:
                break
        l,r = 0, count - 1
        while l < r:
            st[l], st[r] = st[r], st[l]
            l +=1
            r -=1
        return "".join(st)