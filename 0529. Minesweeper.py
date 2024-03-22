class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        visited = set()
        m = len(board)
        n = len(board[0])

        def sweeper(i, j):
            visited.add((i, j))
            if board[i][j] == 'M':
                board[i][j] = 'X'
            elif board[i][j] == 'E':
                p = ((i - 1, j), (i + 1, j), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1), (i, j - 1),
                     (i, j + 1))
                empty = []
                c = 0
                for x, y in p:
                    if 0 <= x < m and 0 <= y < n:
                        if board[x][y] == 'M':
                            c += 1
                        elif (x, y) not in visited:
                            empty.append((x, y))

                if c == 0:
                    board[i][j] = 'B'
                    for x, y in empty:
                        sweeper(x, y)
                else:
                    board[i][j] = str(c)

        sweeper(click[0], click[1])
        return board
