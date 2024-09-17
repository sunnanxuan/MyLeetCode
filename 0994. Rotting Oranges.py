class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.add((i, j))
        res = 0
        while rotten and fresh:
            res += 1
            new = set()
            for i, j in rotten:
                for x, y in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                    if (x, y) in fresh:
                        fresh.discard((x, y))
                        new.add((x, y))
            rotten = new
        if not fresh:
            return res
        else:
            return -1


