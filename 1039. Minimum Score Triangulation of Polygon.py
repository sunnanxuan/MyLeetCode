class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                memo[i, j] = min(
                    [dp(i, k) + dp(k, j) + values[i] * values[j] * values[k] for k in range(i + 1, j)] or [0])
            return memo[i, j]

        return dp(0, len(values) - 1)
