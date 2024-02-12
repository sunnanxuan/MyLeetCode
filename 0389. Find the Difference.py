class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic_s = collections.Counter(s)
        dic_t = collections.Counter(t)
        for k in dic_t:
            if k not in dic_s or dic_s[k] < dic_t[k]:
                return k
