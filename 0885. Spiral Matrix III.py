class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        r = rStart
        c = cStart
        x = 0
        y = 1
        t = 2
        res.append([r, c])
        while len(res) < rows * cols:
            for _ in range(t // 2):
                r += x
                c += y
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            t += 1
            if x == 0 and y == 1:
                x, y = 1, 0
            elif x == 1 and y == 0:
                x, y = 0, -1
            elif x == 0 and y == -1:
                x, y = -1, 0
            elif x == -1 and y == 0:
                x, y = 0, 1
        return res

