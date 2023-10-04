class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        res[0][0] = 1

        def trverse(direction, i, j, l, r, u, d, m):
            if direction == 'R':
                while j < r:
                    j += 1
                    res[i][j] = m
                    m += 1
                if i < d:
                    trverse('D', i, j, l, r, u + 1, d, m)
            elif direction == 'D':
                while i < d:
                    i += 1
                    res[i][j] = m
                    m += 1
                if j > l:
                    trverse('L', i, j, l, r - 1, u, d, m)
            elif direction == 'L':
                while j > l:
                    j -= 1
                    res[i][j] = m
                    m += 1
                if i > u:
                    trverse('U', i, j, l, r, u, d - 1, m)
            elif direction == 'U':
                while i > u:
                    i -= 1
                    res[i][j] = m
                    m += 1
                if j < r:
                    trverse('R', i, j, l + 1, r, u, d, m)

        trverse('R', 0, 0, 0, n - 1, 0, n - 1, 2)
        return res



