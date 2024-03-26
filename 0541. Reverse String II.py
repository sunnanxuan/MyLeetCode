class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        res = []
        while i < len(s):
            res.append(s[i:i + k][::-1])
            res.append(s[i + k:i + 2 * k])
            i += 2 * k
        return ''.join(res)
