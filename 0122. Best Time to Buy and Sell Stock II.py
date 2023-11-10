class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0]*len(prices) for _ in range(2)]
        dp[0][0]=-1*prices[0]
        for i,c in enumerate(prices):
            if i==0:
                continue
            dp[0][i]=max(dp[0][i-1],dp[1][i-1]-c)
            dp[1][i]=max(dp[0][i-1]+c,dp[1][i-1])
        return dp[-1][-1]