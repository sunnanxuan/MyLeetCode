class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n)==1:
            return str(int(n)-1)
        elif n=='10' or n=='11':
            return '9'
        else:
            l=len(n)//2
            m=len(n)%2
            new1=n[:l+m]+n[:l][::-1]
            p2=str(int(n[:l+m])+1)
            new2=p2+p2[:l][::-1]
            p3=str(int(n[:l+m])-1)
            if m==0 and len(p3)<l:
                new3=p3+'9'+p3[:l][::-1]
            else:
                new3=p3+p3[:l][::-1]
            lst=sorted([k for k in [new1,new2,new3] if k!=n],key=lambda x:(abs(int(x)-int(n)),int(x)))
            return lst[0]