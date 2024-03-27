class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        gird=copy.copy(mat)
        zore=False
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    zore=True
                if mat[i][j]==1:
                    if i==0 and j==0:
                        mat[i][j]=mat[i][j]
                    elif i==0:
                        mat[i][j]=1+mat[i][j-1]
                    elif j==0:
                        mat[i][j]=1+mat[i-1][j]
                    else:
                        mat[i][j]=1+min(mat[i][j-1],mat[i-1][j])
                    if not zore:
                        gird[i][j]=float('inf')
                    else:
                        gird[i][j]=mat[i][j]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    continue
                elif i==m-1:
                    mat[i][j]=min(gird[i][j],1+mat[i][j+1])
                elif j==n-1:
                    mat[i][j]=min(gird[i][j],1+mat[i+1][j])
                else:
                    mat[i][j]=min(gird[i][j],1+mat[i+1][j],1+mat[i][j+1])
        return mat