class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1]!=1:
            return False
        memo={}
        def dfs(c,k):
            if c==stones[-1]:
                return True
            elif (c,k) in memo:
                return memo[(c,k)]
            else:
                for n in [k-1,k,k+1]:
                    if n>0 and n+c in stones and dfs(c+n,n):
                        memo[(c,k)]=True
                        return True
                memo[(c,k)]=False
                return False
        return dfs(1,1)
