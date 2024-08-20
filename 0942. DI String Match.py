class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n):
            if s[i] == 'D': dp[i + 1] += (dp[i] + 1)
        for i in range(n - 1, -1, -1):
            if s[i] == 'I': dp[i] += (dp[i + 1] + 1)
        res = [0] * (n + 1)
        arr = [(c, i) for i, c in enumerate(dp)]
        arr.sort()
        for i in range(n + 1):
            _, j = arr.pop()
            res[j] = i
        return res
