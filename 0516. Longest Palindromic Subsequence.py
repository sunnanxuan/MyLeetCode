class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo={}
        def search(l,r):
            if (l,r) in memo:
                return memo[(l,r)]
            if l>r:
                return 0
            elif l==r:
                return 1
            else:
                if s[l]==s[r]:
                    memo[(l,r)]=2+search(l+1,r-1)
                    return memo[(l,r)]
                else:
                    memo[(l,r)]=max(search(l+1,r),search(l,r-1))
                    return memo[(l,r)]
        return search(0,len(s)-1)