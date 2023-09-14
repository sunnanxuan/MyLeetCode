class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        l=0
        res=0
        dic={}
        for r in range(len(s)):
            if s[r] in dic and dic[s[r]]>=l:
                res=max(res,r-l)
                l=dic[s[r]]+1
            dic[s[r]]=r
            e=r
        res=max(res,e-l+1)
        return res
