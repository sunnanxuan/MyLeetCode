class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        m=0
        for n in num:
            m=m*10+n
        m+=k
        res=[]
        while m:
            res.append(m%10)
            m//=10
        return res[::-1]
