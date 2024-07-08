class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n=len(arr)
        up=[0]*n
        down=[0]*n
        res=0
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                up[i]+=up[i-1]+1
        for j in range(n-2,-1,-1):
            if arr[j]>arr[j+1]:
                down[j]+=down[j+1]+1
            if down[j] and up[j]:
                res=max(res,down[j]+up[j]+1)
        return res