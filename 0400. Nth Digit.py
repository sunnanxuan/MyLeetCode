class Solution:
    def findNthDigit(self, n: int) -> int:
        m=0
        c=0
        step=0
        pre=0
        while n>c:
            step+=1
            m+=(1+pre)*9
            c+=((1+pre)*9)*step
            pre=m
        ind=step-(1+(c-n)%(step))
        return int(str(m-(c-n)//(step))[ind])