class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        if m*n!=r*c:return mat
        data=[]
        for l in mat:
            data.extend(l)
        newmat=[]
        for i in range(r):
            newmat.append(data[i*c:(i+1)*c])
        return newmat