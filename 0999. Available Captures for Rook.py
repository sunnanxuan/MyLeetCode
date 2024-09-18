class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        res = 0
        m = len(board)
        n = len(board[0])
        for i in range(m):
            if 'R' in board[i]:
                j = board[i].index('R')
                h = [[j - 1, -1, -1], [j + 1, n, 1]]
                for a, b, s in h:
                    for c in range(a, b, s):
                        if board[i][c] == 'B':
                            break
                        elif board[i][c] == 'p':
                            res += 1
                            break
                v = [[i - 1, -1, -1], [i + 1, m, 1]]
                for a, b, s in v:
                    for c in range(a, b, s):
                        if board[c][j] == 'B':
                            break
                        elif board[c][j] == 'p':
                            res += 1
                            break
        return res
