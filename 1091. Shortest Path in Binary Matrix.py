class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        if grid[0][0]==1 or grid[-1][-1]==1:return -1
        res=1
        q=[(0,0)]
        move=((-1,0),(1,0),(-1,-1),(0,-1),(1,-1),(-1,1),(0,1),(1,1))
        visited=set()
        visited.add((0,0))
        while q:
            new=[]
            for i,j in q:
                if i==m-1 and j==n-1:return res
                for x,y in move:
                    if 0<=i+x<m and 0<=j+y<n and grid[i+x][j+y]==0 and (i+x,j+y) not in visited:
                        new.append((i+x,j+y))
                        visited.add((i+x,j+y))
            res+=1
            q=new
        return -1
