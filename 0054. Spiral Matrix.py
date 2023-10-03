class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = [matrix[0][0]]

        def trverse(direction, i, j, l, r, u, d):
            if direction == 'R':
                while j < r:
                    j += 1

                    res.append(matrix[i][j])
                if i < d:
                    trverse('D', i, j, l, r, u + 1, d)
            elif direction == 'D':
                while i < d:
                    i += 1
                    res.append(matrix[i][j])
                if j > l:
                    trverse('L', i, j, l, r - 1, u, d)
            elif direction == 'L':
                while j > l:
                    j -= 1
                    res.append(matrix[i][j])
                if i > u:
                    trverse('U', i, j, l, r, u, d - 1)
            elif direction == 'U':
                while i > u:
                    i -= 1
                    res.append(matrix[i][j])
                if j < r:
                    trverse('R', i, j, l + 1, r, u, d)

        trverse('R', 0, 0, 0, len(matrix[0]) - 1, 0, len(matrix) - 1)
        return res
