class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        attack=[set(),set(),set()]
        board=[["."]*n for _ in range(n)]
        def dfs(i,attack,board):

            for j in range(n):
                if all(j not in s for s in attack):
                    newboard=copy.deepcopy(board)
                    newboard[i][j]='Q'
                    if i==n-1:
                        arr=[]
                        for lst in newboard:
                            arr.append("".join(lst))
                        res.append(arr)
                    else:
                        l=set()

                        r=set()
                        for k in attack[0]:
                            if k-1>=0:l.add(k-1)
                        if j-1>=0:l.add(j-1)
                        for k in attack[2]:
                            if k+1<n:r.add(k+1)
                        if j+1<n:r.add(j+1)
                        m=attack[1]|{j}

                        dfs(i+1,[l,m,r],newboard)
        dfs(0,attack,board)
        return res
