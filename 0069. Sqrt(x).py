class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        elif 1<=x<4:
            return 1
        n=2
        while n*n<=x:
            m=n*n
            while m*m<=x:
                n=m
                m*=m
            n+=1
        return n-1
