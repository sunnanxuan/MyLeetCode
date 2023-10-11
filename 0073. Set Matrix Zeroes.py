class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        arr=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    for x in range(len(matrix)):
                        arr.add((x,j))
                    for y in range(len(matrix[0])):
                        arr.add((i,y))
        for i,j in arr:
            matrix[i][j]=0
        return matrix