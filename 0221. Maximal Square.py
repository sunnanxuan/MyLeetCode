class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(0,m):
            for j in range(0,n):
                if i==0 or j==0 or matrix[i][j]=='0':
                    matrix[i][j]=int(matrix[i][j])
                elif matrix[i][j]=='1':
                    matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+int(matrix[i][j])
        return max([max(matrix[i]) for i in range(m)])**2