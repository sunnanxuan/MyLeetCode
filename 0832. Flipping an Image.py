class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        res=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if image[i][j]==0:
                    p=-1*j-1
                    res[i][p]=1
        return res
