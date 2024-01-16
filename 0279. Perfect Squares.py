class Solution:
    def numSquares(self, n: int) -> int:
        square=[]
        m=int(n**0.5)
        for i in range(m,0,-1):
            square.append(i**2)
        res=[float('inf')]
        def add(sm,i,c):
            if c>=res[0] or sm>n:
                return
            if sm==n:
                res[0]=min(res[0],c)
            elif sm<n:
                for j in range(i,len(square)):
                    add(sm+square[j],j,c+1)
        add(0,0,0)
        return res[0]
