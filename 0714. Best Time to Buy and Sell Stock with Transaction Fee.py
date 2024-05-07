class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [-1 * prices[0] - fee, 0]
        for p in prices[1:]:
            dp[0], dp[1] = max(dp[1] - p - fee, dp[0]), max(dp[0] + p, dp[1])
        return dp[1]
