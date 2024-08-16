class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=copy.copy(matrix[0])
        for i in range(m-1):
            new=[0]*n
            for j in range(n):
                new[j]=matrix[i+1][j]+min(dp[j],dp[max(j-1,0)],dp[min(n-1,j+1)])
            dp=new
        return min(dp)