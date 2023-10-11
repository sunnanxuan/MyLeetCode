
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0]<=target<=row[-1]:
                p=bisect.bisect_left(row,target)
                if target==row[p]:
                    return True
                else:
                    False
        return False