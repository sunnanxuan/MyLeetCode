class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        dp = [-1] * (amount + 1)
        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                arr = [dp[i - j] for j in coins if j < i and dp[i - j] != -1]
                if arr:
                    dp[i] = 1 + min(arr)

        return dp[-1]
