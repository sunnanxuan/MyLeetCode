class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = collections.Counter(s)
        dic_t = collections.Counter(t)
        return dic_s == dic_t
