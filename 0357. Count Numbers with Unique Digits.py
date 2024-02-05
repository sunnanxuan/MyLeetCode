class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            c=9
            for j in range(1,i):
                c*=(10-j)
            dp[i]=dp[i-1]+c
        return dp[n]