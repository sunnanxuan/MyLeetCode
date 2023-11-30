class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo={}
        def match(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==len(s):
                if j==len(p):
                    memo[(i,j)]=True
                    return True
                elif p[j]!='*':
                    memo[(i,j)]=False
                    return False
                elif p[j]=='*':
                    memo[(i,j)]=match(i,j+1)
                    return memo[(i,j)]
            elif j==len(p):
                memo[(i,j)]=False
                return False
            if p[j]=='*':
                memo[(i,j)]=(match(i+1,j) or match(i,j+1) or match(i+1,j+1))
                return memo[(i,j)]
            elif s[i]==p[j] or p[j]=='?':
                memo[(i,j)]=match(i+1,j+1)
                return memo[(i,j)]
            elif s[i]!=p[j]:
                memo[(i,j)]=False
                return False
        return match(0,0)