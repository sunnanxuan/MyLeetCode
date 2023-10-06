class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: return 0
        matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    matrix[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                elif i == 0:
                    matrix[i][j] = matrix[i][j - 1]
                elif j == 0:
                    matrix[i][j] = matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[-1][-1]
