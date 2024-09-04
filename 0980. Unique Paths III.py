class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        squares = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    r = i
                    c = j
                elif grid[i][j] == 2:
                    t = (i, j)
                    squares.add((i, j))
                elif grid[i][j] == 0:
                    squares.add((i, j))

        def path(i, j, unvisited):
            if (i, j) == t:
                if not unvisited:
                    return 1
                else:
                    return 0
            else:
                res = 0
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if (x, y) in unvisited:
                        res += path(x, y, unvisited - {(x, y)})
                return res

        return path(r, c, squares)
