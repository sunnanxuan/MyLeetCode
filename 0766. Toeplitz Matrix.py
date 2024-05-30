class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            x=i
            y=0
            while x<m-1 and y<n-1:
                if matrix[x][y]!=matrix[x+1][y+1]:return False
                else:
                    x+=1
                    y+=1
        for j in range(n):
            x=0
            y=j
            while x<m-1 and y<n-1:
                if matrix[x][y]!=matrix[x+1][y+1]:return False
                else:
                    x+=1
                    y+=1
        return True