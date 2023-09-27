class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=[[board[i][j] for j in range(9) if board[i][j]!="."] for i in range(9)]
        col=[[board[i][j] for i in range(9) if board[i][j]!="."] for j in range(9) ]
        matrix=[[board[i][j] for i in range(m*3,(m+1)*3) for j in range(n*3,(n+1)*3) if board[i][j]!="."] for m in range(3) for n in range(3)]
        spaces=[(i,j) for i in range(9) for j in range(9) if board[i][j]=="."]
        def dfs(i):
            if i==len(spaces):
                return True
            x=spaces[i][0]
            y=spaces[i][1]
            for n in ['1','2','3','4','5','6','7','8','9']:
                if n not in row[x] and n not in col[y] and n not in matrix[3*(x//3)+(y//3)]:
                    row[x].append(n)
                    col[y].append(n)
                    matrix[3*(x//3)+(y//3)].append(n)
                    if dfs(i+1):
                        board[x][y]=n
                        return True
                    else:
                        row[x].pop()
                        col[y].pop()
                        matrix[3*(x//3)+(y//3)].pop()
            return False
        dfs(0)
        return board