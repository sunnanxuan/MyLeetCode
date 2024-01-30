class Solution:
    def integerBreak(self, n: int) -> int:
        memo={}
        def numbreak(n):
            if n in memo:
                return memo[n]
            if n<=4:return n
            else:
                memo[n]=max(3*numbreak(n-3),2*numbreak(n-2))
                return memo[n]

        if n==2:return 1
        elif n==3:
            return 2
        else:
            return numbreak(n)