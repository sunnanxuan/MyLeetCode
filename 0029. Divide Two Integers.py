class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=0
        neg=False
        if dividend*divisor<0:
            neg=True
        dividend=abs(dividend)
        divisor=abs(divisor)
        while dividend>=divisor:
            i=0
            while divisor<<i <= dividend:
                i+=1
            i-=1
            res+=(1<<i)
            dividend-=(divisor<<i)
        if neg:res=-res
        return min(2**31-1,max(-2**31,res))