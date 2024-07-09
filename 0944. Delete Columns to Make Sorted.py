class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs[0])
        m=len(strs)
        res=0
        for j in range(n):
            for i in range(1,m):
                if strs[i][j]<strs[i-1][j]:break
            else:continue
            res+=1
        return res