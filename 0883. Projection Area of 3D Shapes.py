class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        res=sum([grid[i][j]!=0 for i in range(m) for j in range(n)])
        for i in range(m):
            res+=max(grid[i])
        for j in range(n):
            res+=max([grid[i][j] for i in range(m)])
        return res