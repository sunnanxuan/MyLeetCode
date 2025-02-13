class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        res = ""
        left = 0
        while last:
            right = min(last.values())
            c, i = min((s[i], i) for i in range(left, right + 1) if s[i] not in res)
            left = i + 1
            res += c
            del last[c]
        return res


