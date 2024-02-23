class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        cur = 1
        while n >= cur:
            n -= cur
            cur += 1
            res += 1
        return res
