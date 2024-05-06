class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                res += 1
                r = s[i]
                l = s[i - 1]
                j = 1
                while i - 1 - j >= 0 and i + j < len(s) and s[i + j] == r and s[i - 1 - j] == l:
                    res += 1
                    j += 1
        return res
