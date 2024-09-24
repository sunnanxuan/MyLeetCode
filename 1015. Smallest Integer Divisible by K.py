class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        res = 1
        n = 1
        if str(k)[-1] not in ['1', '3', '7', '9']: return -1
        while n % k:
            n %= k
            res += 1
            n *= 10
            n += 1
        return res
