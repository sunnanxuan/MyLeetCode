class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        res = 1

        i = 0
        while i < abs(n):
            if abs(n) - i == 1:
                res *= x
                i += 1
            else:
                j = 2
                q = x
                while j <= abs(n) - i:
                    q = q * q
                    j *= 2
                res *= q
                i += (j // 2)

        if n > 0:
            return res
        else:
            return 1 / res


