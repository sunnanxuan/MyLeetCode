class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        lst=sorted(arr, reverse=True)
        n=len(arr)
        res=[]
        for i,c in enumerate(lst):
            j=arr.index(c)
            if j==n-1-i:continue
            else:
                res.append(j+1)
                arr[:j+1]=arr[:j+1][::-1]
                res.append(n-i)
                arr[:n-i]=arr[:n-i][::-1]
        return res
