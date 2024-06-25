class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def findisland(i, j):
            res = {(i, j)}
            visited.add((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (x, y) not in visited:
                    res |= findisland(x, y)
            return res

        visited = set()
        res = 0
        islands = {}
        ind = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    cur = findisland(i, j)
                    l = len(cur)
                    for p in cur:
                        islands[p] = [ind, l]
                    ind += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    used = set()
                    c = 1
                    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and islands[(x, y)][0] not in used:
                            c += islands[(x, y)][1]
                            used.add(islands[(x, y)][0])
                    res = max(res, c)
        return res and res or m * n