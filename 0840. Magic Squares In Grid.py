class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3: return 0
        res = 0
        for i in range(m - 2):
            for j in range(n - 2):
                arr = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if len(set(arr)) < 9 or any([s < 1 or s > 9 for s in arr]): continue
                h1 = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                h2 = grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2]
                h3 = grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                v1 = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
                v2 = grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]
                v3 = grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]
                d1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
                d2 = grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2]
                if all([c == 15 for c in (h1, h2, h3, v1, v2, v3, d1, d2)]):
                    res += 1
        return res
