class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp=[[0]*(amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0]=1
        for i in range(len(coins)):
            for j in range(1,amount+1):
                if i==0:
                    if j>=coins[i]:
                        dp[i][j]=dp[i][j-coins[i]]
                else:
                    if j>=coins[i]:
                        dp[i][j]=dp[i][j-coins[i]]+dp[i-1][j]
                    else:
                        dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
