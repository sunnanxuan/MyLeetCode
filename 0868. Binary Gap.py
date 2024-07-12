class Solution:
    def binaryGap(self, n: int) -> int:
        p=cur=0
        res=0
        while n:
            cur+=1
            if n%2:
                if p:res=max(res,cur-p)
                p=cur
            n//=2
        return res