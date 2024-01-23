class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[1]*n for _ in range(m)]
        change=True
        while change:
            change=False
            for i in range(m):
                for j in range(n):
                    new=1+max([dp[x][y] for x,y in ((i-1,j),(i,j-1),(i+1,j),(i,j+1)) if 0<=x<m and 0<=y<n and matrix[x][y]>matrix[i][j]],default=0)
                    if new>dp[i][j]:
                        dp[i][j]=new
                        change=True
        res=max([max(lst) for lst in dp])
        return res