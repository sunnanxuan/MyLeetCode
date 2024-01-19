class NumMatrix:

    def __init__(self, matrix):
        self.sm = matrix
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                self.sm[i][j] += self.sm[i][j - 1]
        for j in range(n):
            for i in range(1, m):
                self.sm[i][j] += self.sm[i - 1][j]

    def sumRegion(self, row1, col1, row2, col2):
        if row1 == col1 == 0:
            return self.sm[row2][col2]
        elif row1 == 0:
            return self.sm[row2][col2] - self.sm[row2][col1 - 1]
        elif col1 == 0:
            return self.sm[row2][col2] - self.sm[row1 - 1][col2]
        else:
            return self.sm[row2][col2] - self.sm[row2][col1 - 1] - self.sm[row1 - 1][col2] + self.sm[row1 - 1][col1 - 1]