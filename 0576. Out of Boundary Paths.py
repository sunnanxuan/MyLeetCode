class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo={}
        mod=10**9+7
        def path(i,j,p):
            if (i,j,p) in memo:
                return memo[(i,j,p)]
            if p==0:
                return 0
            elif p>0:
                c=0
                for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if x==-1 or y==-1 or x==m or y==n:
                        c+=1
                    else:
                        c+=path(x,y,p-1)
            memo[(i,j,p)]=c%mod
            return memo[(i,j,p)]
        return path(startRow,startColumn,maxMove)