class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = collections.Counter(s)
        for i, c in enumerate(s):
            if dic[c] == 1:
                return i
        return -1
