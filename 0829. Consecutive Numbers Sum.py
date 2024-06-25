class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res=1
        for m in range(2,n+1):
            c=(2*n/m-m+1)/2
            if c<1:break
            if int(c)==c:
                res+=1
        return res