class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        memo={}
        def flip(pre,i):
            if i==len(s):return 0
            if (pre,i) in memo:return memo[(pre,i)]
            if pre=='1':
                if s[i]==pre:
                    memo[(pre,i)]=flip(pre,i+1)
                else:
                    memo[(pre,i)]=1+flip(pre,i+1)
            else:
                if s[i]==pre:
                    memo[(pre,i)]=flip(pre,i+1)
                else:
                    memo[(pre,i)]=min(1+flip(pre,i+1),flip('1',i+1))
            return memo[(pre,i)]
        return min(flip('0',0),flip('1',0))
