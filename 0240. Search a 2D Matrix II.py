class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        visited=set()
        def find(i,j):
            if i<m and j<n and (i,j) not in visited:
                visited.add((i,j))
                if matrix[i][j]==target:
                    return True
                elif matrix[i][j]<target:
                    return any([find(i+1,j),find(i,j+1)])
                elif matrix[i][j]>target:
                    return False
            else:
                return False
        return find(0,0)