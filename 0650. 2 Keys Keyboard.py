class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        while n > 1:
            for i in range(2, n + 1):
                if n % i == 0:
                    res += i
                    n //= i
                    break
        return res
