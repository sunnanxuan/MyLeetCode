class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        seen={grid[0][0]}
        heap=[(grid[0][0],0,0)]
        visited={grid[0][0]}
        def swim(i,j):
            for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0<=x<m and 0<=y<n and grid[x][y] not in seen:
                    seen.add(grid[x][y])
                    heapq.heappush(heap,(grid[x][y],x,y))
            mn,r,c=heapq.heappop(heap)
            if mn==grid[-1][-1]:
                visited.add(mn)
                return
            else:
                visited.add(mn)
                swim(r,c)
        swim(0,0)
        return max(visited)