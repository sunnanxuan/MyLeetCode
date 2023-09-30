class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:]=[[matrix[i][j] for i in range(len(matrix)-1,-1,-1)] for j in range(len(matrix)) ]
