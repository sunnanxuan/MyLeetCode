class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if m < n:
            return 0
        dp = [[0] * n for _ in range(m)]
        p = 0
        for i in range(n):
            find = False
            for j in range(i, m):

                if j < p:
                    continue
                elif j >= p:
                    if t[i] == s[j]:
                        if j == i == 0:
                            dp[j][i] = 1
                        elif i == 0:
                            dp[j][i] = 1 + dp[j - 1][i]
                        else:
                            dp[j][i] = dp[j - 1][i] + dp[j - 1][i - 1]
                    else:
                        if j == 0:
                            dp[j][i] = 0
                        else:
                            dp[j][i] = dp[j - 1][i]

                    if dp[j][i] > 0 and not find:
                        p = j + 1
                        find = True
            if not find:
                return 0
        return dp[-1][-1]
