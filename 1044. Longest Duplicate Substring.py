class Solution:
    def longestDupSubstring(self, s: str) -> str:
        A = [ord(c) - ord('a') for c in s]
        mod = 2 ** 63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(s)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)

        res, lo, hi = 0, 0, len(s)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return s[res:res + lo]


1

