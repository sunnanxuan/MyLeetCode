class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        heap = []

        def island(i, j):
            heap.append((0, i, j))
            visited.add((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and (x, y) not in visited: island(x, y)

        for i in range(m):
            if heap: break
            for j in range(n):
                if grid[i][j] == 1:
                    island(i, j)
                    break

        heapq.heapify(heap)
        while heap:
            cur = heapq.heappop(heap)
            c, i, j = cur
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:

                    if grid[x][y] == 1: return c
                    heapq.heappush(heap, (c + 1, x, y))
                    visited.add((x, y))


