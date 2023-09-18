class Solution:
    def reverse(self, x: int) -> int:
        s=""
        if x<0:
            s+='-'
            x*=-1
        s=s+str(x)[::-1]
        res=int(s)
        if -2**31 <= res <= 2**31 - 1:return res
        else:return 0