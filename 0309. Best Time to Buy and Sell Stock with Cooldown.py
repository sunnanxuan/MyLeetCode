class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0][0] = -1 * prices[0]
        for i in range(1, len(prices)):
            if dp[i - 1][2] == 0:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 2][1] - prices[i])
            if dp[i - 1][0] + prices[i] > dp[i - 1][1]:
                dp[i][1] = dp[i - 1][0] + prices[i]
                dp[i][2] = 1
            else:
                dp[i][1] = dp[i - 1][1]

        return dp[-1][1]
