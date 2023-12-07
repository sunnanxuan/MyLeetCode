class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m=len(dungeon)
        n=len(dungeon[0])
        grid=[[0]*n for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    grid[i][j]=max(1,1-dungeon[i][j])
                elif i==m-1:
                    grid[i][j]=max(1,grid[i][j+1]-dungeon[i][j])
                elif j==n-1:
                    grid[i][j]=max(1,grid[i+1][j]-dungeon[i][j])
                else:
                    grid[i][j]=max(1,min(grid[i+1][j]-dungeon[i][j],grid[i][j+1]-dungeon[i][j]))
        return grid[0][0]