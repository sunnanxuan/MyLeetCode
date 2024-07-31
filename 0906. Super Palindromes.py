class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        res=0
        l=math.ceil(int(left)**0.5)
        r=int(int(right)**0.5)
        for i in range(max(0,int(l)),min(int(r)+1,10)):
            c=str(i**2)
            if int(left)<=i**2<=int(right) and c==c[::-1]:
                res+=1
        L=str(l)
        R=str(r)
        hl=len(L)//2
        hr=len(R)//2
        for j in range(int(10**(hl-1)),10**hr):
            c=str(j)
            for n in ['','0','1','2','3','4','5','6','7','8','9']:
                s=c+n+c[::-1]
                if l<=int(s)<=r:
                    p=int(s)**2
                    if int(left)<=p<=int(right) and str(p)==str(p)[::-1]:res+=1
                    elif int(s)>r:break
        return res
