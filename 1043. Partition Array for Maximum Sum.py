class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * len(arr)
        for i in range(len(arr)):
            if i < k:
                dp[i] = max(arr[:i + 1]) * (i + 1)
            else:
                cur = arr[i] + dp[i - 1]
                for j in range(i - k + 1, i):
                    mx = max(arr[j:i + 1])
                    cur = max(cur, mx * (i - j + 1) + dp[j - 1])
                dp[i] = cur
        return dp[-1]

