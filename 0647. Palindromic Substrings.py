class Solution:
    def countSubstrings(self, s: str) -> int:
        memo={}
        def palindromic(l,r):
            if (l,r) in memo:return memo[(l,r)]
            if l==r:
                memo[(l,r)]=True
            elif l==r-1:
                if s[l]==s[r]:memo[(l,r)]=True
                else:memo[(l,r)]=False
            else:
                if palindromic(l+1,r-1) and s[l]==s[r]:memo[(l,r)]=True
                else:memo[(l,r)]=False
            return memo[(l,r)]
        for l in range(len(s)):
            for r in range(l,len(s)):
                palindromic(l,r)
        return sum(list(memo.values()))