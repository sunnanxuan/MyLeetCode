class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        grid = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                sm = sum([0 <= x < m and 0 <= y < n and board[x][y] == 1 for x, y in (
                (i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                (i + 1, j + 1))])
                if board[i][j] == 0:
                    if sm == 3:
                        grid[i][j] = 1
                elif board[i][j] == 1:
                    if sm == 2 or sm == 3:
                        grid[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = grid[i][j]

