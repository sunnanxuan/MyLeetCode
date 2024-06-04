class Solution:
    def numTilings(self, n: int) -> int:
        dp=[0,1,2,5,11]
        mod=10**9+7
        for i in range(5,n+1):
            m=1*dp[i-1]+1*dp[i-2]+2*dp[i-3]
            p=0
            for j in range(4,i):
                m+=2*dp[i-j]
            m+=2
            dp.append(m%mod)
        return dp[n]