class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n = str(n)
        res = 0
        l = len(digits)
        for i in range(1, len(n)):
            res += (l ** i)
        j = 0
        while j < len(n):
            p = bisect.bisect_left(digits, n[j])
            res += (p * l ** (len(n) - j - 1))
            if p < l and digits[p] == n[j]:
                if j == len(n) - 1: res += 1
                j += 1
            else:
                break
        return res
