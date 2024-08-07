class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        p = 0
        for c in s:
            if c == '(':
                p += 1
            elif c == ')':
                p -= 1
            if p < 0:
                res += 1
                p += 1
        res += abs(p)
        return res
