class Solution:
    def countDigitOne(self, n: int) -> int:
        k=0
        l=n//10
        r=0
        cur=n%10
        res=0
        while l or cur:
            if cur==0:
                res+=l*10**k
            elif cur==1:
                res+=l*10**k+r+1
            else:
                res+=(l+1)*10**k
            r+=cur*10**k
            cur=l%10
            l//=10
            k+=1
        return res
