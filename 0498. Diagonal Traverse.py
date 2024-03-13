class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        m = len(mat)
        n = len(mat[0])
        i = j = 0
        dir_i = -1
        dir_j = 1
        while len(res) < m * n:
            res.append(mat[i][j])
            i += dir_i
            j += dir_j
            if i < 0 or j == n:
                if j == n:
                    j -= 1
                    i += 2
                else:
                    i += 1
                dir_i *= -1
                dir_j *= -1
            elif j < 0 or i == m:
                if i == m:
                    i -= 1
                    j += 2
                else:
                    j += 1
                dir_i *= -1
                dir_j *= -1
        return res
