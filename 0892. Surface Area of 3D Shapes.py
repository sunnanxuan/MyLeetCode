class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i == j == 0:
                        res += (2 + 4 * grid[i][j])
                    elif i == 0:
                        res += (2 + 4 * grid[i][j] - 2 * min(grid[i][j], grid[i][j - 1]))
                    elif j == 0:
                        res += (2 + 4 * grid[i][j] - 2 * min(grid[i][j], grid[i - 1][j]))
                    else:
                        res += (2 + 4 * grid[i][j] - 2 * min(grid[i][j], grid[i][j - 1]) - 2 * min(grid[i][j],
                                                                                                   grid[i - 1][j]))

        return res

