class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m=len(img)
        n=len(img[0])
        res=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                sm=0
                c=0
                for x,y in ((i-1,j),(i-1,j-1),(i-1,j+1),(i,j-1),(i,j+1),(i,j),(i+1,j-1),(i+1,j),(i+1,j+1)):
                    if 0<=x<m and 0<=y<n:
                        c+=1
                        sm+=img[x][y]
                res[i][j]=sm//c
        return res