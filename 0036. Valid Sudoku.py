class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[[board[i][j] for j in range(9) if board[i][j]!="."] for i in range(9)]
        for r in row:
            if len(r)>len(set(r)):
                return False
        col=[[board[i][j] for i in range(9) if board[i][j]!="."] for j in range(9) ]
        for c in col:
            if len(c)>len(set(c)):
                return False
        matrix=[[board[i][j] for i in range(m*3,(m+1)*3) for j in range(n*3,(n+1)*3) if board[i][j]!="."] for m in range(3) for n in range(3)]
        for m in matrix:
            if len(m)>len(set(m)):
                return False
        return True
