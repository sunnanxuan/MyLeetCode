class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def move(i, j):
            grid[i][j] = 0
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and (x, y) and grid[x][y] == 1:
                    move(x, y)

        m = len(grid)
        n = len(grid[0])
        for i in [0, m - 1]:
            for j in range(n):
                if grid[i][j] == 1:
                    move(i, j)
        for j in [0, n - 1]:
            for i in range(m):
                if grid[i][j] == 1:
                    move(i, j)

        return sum([row.count(1) for row in grid])