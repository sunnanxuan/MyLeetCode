class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n=len(grid)
        row=[0]*n
        col=[0]*n
        for i in range(n):
            row[i]=max(grid[i])
            col[i]=max([grid[j][i] for j in range(n)])
        res=0
        for i in range(n):
            for j in range(n):
                res+=min(row[i],col[j])-grid[i][j]
        return res
