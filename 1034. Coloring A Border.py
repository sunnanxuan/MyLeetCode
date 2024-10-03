class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:


        m=len(grid)
        n=len(grid[0])
        used=set()
        def find(i,j):
            used.add((i,j))
            for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0<=x<m and 0<=y<n and (x,y) not in used and grid[x][y]==grid[row][col]:
                    find(x,y)

        find(row,col)
        for i,j in used:
            if any(x<0 or x==m or y<0 or y==n or (x,y) not in used for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1))):
                grid[i][j]=color
        return grid