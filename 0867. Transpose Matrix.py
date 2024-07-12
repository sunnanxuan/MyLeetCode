class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        res=[[matrix[i][j] for i in range(m)] for j in range(n)]
        return res