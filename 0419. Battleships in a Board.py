class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                        res += 1
                        board[i][j] = 'B'
                    elif board[i - 1][j] == 'B' and board[i][j - 1] == 'B':
                        board[i][j] = 'B'
                    elif board[i - 1][j] == 'B' or board[i - 1][j] == 'V':
                        board[i - 1][j] == 'V'
                        board[i][j] = 'V'
                    elif board[i - 1][j] == 'H':
                        res += 1
                        board[i][j] = 'B'
                    elif board[i][j - 1] == 'B' or board[i][j - 1] == 'H':
                        board[i][j - 1] == 'H'
                        board[i][j] = 'H'
                    elif board[i][j - 1] == 'V':
                        res += 1
                        board[i][j] = 'B'
        return res
