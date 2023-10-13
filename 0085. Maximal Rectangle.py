class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':

                    if i == 0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = 1 + matrix[i - 1][j]
                    k = j - 1
                    h = matrix[i][j]
                    res = max(h, res)
                    while k >= 0 and matrix[i][k] > 0:
                        h = min(h, matrix[i][k])
                        res = max(res, h * (j - k + 1))
                        k -= 1
                else:
                    matrix[i][j] = 0
        return res
