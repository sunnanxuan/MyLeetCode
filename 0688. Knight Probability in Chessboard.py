class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        memo={}
        def move(c,i,j):
            if (c,i,j) in memo:return memo[(c,i,j)]
            if i<0 or i>=n or j<0 or j>=n:return 0
            elif c==0:return 1
            else:
                memo[(c,i,j)]=sum([move(c-1,x,y) for x,y in ((i-2,j-1),(i-1,j-2),(i-2,j+1),(i-1,j+2),(i+1,j-2),(i+2,j-1),(i+2,j+1),(i+1,j+2))])/8
                return memo[(c,i,j)]
        return move(k,row,column)