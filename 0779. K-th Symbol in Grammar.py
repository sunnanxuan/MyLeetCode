class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        inds=[]
        m=n
        while m>1:
            inds.append(k)
            k=k//2+k%2
            m-=1
        dic={0:[1,0],1:[0,1]}
        s=0
        while inds:
            c=inds.pop()
            s=dic[s][c%2]
        return s