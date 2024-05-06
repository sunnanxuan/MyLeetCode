class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def search(i,j):
            visited.add((i,j))
            sm=1
            for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0<=x<m and 0<=y<n and grid[x][y]==1 and (x,y) not in visited:
                    sm+=search(x,y)
            return sm
        res=0
        visited=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 or (i,j) in visited:continue
                else:
                    res=max(res,search(i,j))
        return res