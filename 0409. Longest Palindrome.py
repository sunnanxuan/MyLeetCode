class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic=collections.Counter(s)
        res=0
        for v in dic.values():
            res+=(v//2)*2
        if res<len(s):
            res+=1
        return res
