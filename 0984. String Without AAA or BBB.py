class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res=[]
        if a>=b:m,n,c1,c2=a,b,'a','b'
        elif b>a:m,n,c1,c2=b,a,'b','a'
        q,d=divmod(m,n+1)
        for i in range(d):
            res.append(c1*(q+1))
            res.append(c2)
        for j in range(n+1-d):
            res.append(c1*q)
            res.append(c2)
        res.pop()
        return ''.join(res)
