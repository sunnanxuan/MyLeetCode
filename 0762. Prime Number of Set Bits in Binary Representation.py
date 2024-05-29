class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        memo = {}
        memo[0] = False
        memo[1] = False

        def isprime(m):
            if m in memo:
                return memo[m]
            else:
                i = 2
                while i <= m ** 0.5:
                    if m % i:
                        i += 1
                    else:
                        memo[m] = False
                        return False
                memo[m] = True
                return True

        res = 0
        for n in range(left, right + 1):
            num = bin(n)[2:]
            m = num.count('1')
            if isprime(m):
                res += 1
        return res
