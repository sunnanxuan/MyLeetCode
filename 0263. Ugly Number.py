class Solution:
    def isUgly(self, n: int) -> bool:
        change = True
        while n > 1 and change:
            change = False
            for f in [2, 3, 5]:
                if n % f == 0:
                    change = True
                    n //= f
        return n == 1
