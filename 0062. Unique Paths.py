class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==j==0:
                    matrix[i][j]=1
                elif i==0:
                    matrix[i][j]=matrix[i][j-1]
                elif j==0:
                    matrix[i][j]=matrix[i-1][j]
                else:
                    matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
        return matrix[-1][-1]