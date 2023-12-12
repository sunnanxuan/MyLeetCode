class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        res=0
        def search(x,y):
            visited.add((x,y))
            for i,j in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if 0<=i<m and 0<=j<n and (i,j) not in visited:
                    if grid[i][j]=='1':
                        search(i,j)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in visited:
                    res+=1
                    search(i,j)
        return res