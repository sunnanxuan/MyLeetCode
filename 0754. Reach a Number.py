class Solution:
    def reachNumber(self, target: int) -> int:
        t=abs(target)
        sm=0
        res=0
        i=1
        while sm<t or (sm-t)%2:
            sm+=i
            i+=1
            res+=1
        return res