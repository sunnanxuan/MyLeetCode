class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0,0,0,0] for _ in range(len(prices))]
        for i,p in enumerate(prices):
            if i==0:
                dp[0][0]=-p
            else:
                dp[i][0]=max(dp[i-1][0],-p)
                dp[i][1]=max(dp[i-1][1],dp[i][0]+p)
                if i==2:
                    dp[i][2]=dp[i-1][1]-p
                elif i>2:
                    dp[i][2]=max(dp[i-1][2],dp[i-1][1]-p)
                    dp[i][3]=max(dp[i-1][3],dp[i-1][2]+p)
        return max(dp[-1][-1],dp[-1][-3])