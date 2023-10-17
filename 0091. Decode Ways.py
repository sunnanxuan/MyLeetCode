class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)

        if s[0] == '0' or '00' in s:
            return 0
        else:
            dp[0] = 1
        if len(s) >= 2:
            if int(s[0:2]) <= 26 and s[1] != '0':
                dp[1] = 2
            elif int(s[0:2]) > 26 and s[1] == '0':
                return 0
            else:
                dp[1] = 1
        for i in range(2, len(s)):
            if int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
                if s[i] == '0':
                    dp[i] = dp[i - 2]
                else:
                    dp[i] = dp[i - 1] + dp[i - 2]
            else:
                if s[i] == '0':
                    return 0
                else:
                    dp[i] = dp[i - 1]
