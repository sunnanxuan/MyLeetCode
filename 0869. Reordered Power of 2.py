class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        c=str(n)
        dic_n=collections.Counter(c)
        l=len(c)
        mn=int(math.log2(10**(l-1)))
        mx=int(math.log2(10**l-1))
        for i in range(mn,mx+1):
            q=2**i
            dic=collections.Counter(str(q))
            if dic==dic_n:return True
        return False