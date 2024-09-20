class Solution:
    def clumsy(self, n: int) -> int:

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            res = n * (n - 1) // (n - 2)
            n -= 3
            while n > 3:
                res += n
                n -= 1
                res -= n * (n - 1) // (n - 2)
                n -= 3
            if n:
                res += n
                n -= 1
            if n: res -= n
            return res
