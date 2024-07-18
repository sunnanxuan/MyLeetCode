class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_set=set(arr)
        def count(n1,n2):
            c=2
            while n1+n2 in arr_set:
                n1,n2=n2,n1+n2
                c+=1
            return c
        res=0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                res=max(res,count(arr[i],arr[j]))
        return res>2 and res or 0