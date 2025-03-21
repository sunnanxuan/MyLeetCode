class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                if s[i] == s[j]:
                    is_palindrome[i][j] = True if L == 2 else is_palindrome[i + 1][j - 1]

        dp = [len(s)] * (len(s) + 1)
        dp[0] = -1
        dp[1] = 0
        for i in range(2, len(s) + 1):
            for j in range(0, i):
                if is_palindrome[j][i - 1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]


