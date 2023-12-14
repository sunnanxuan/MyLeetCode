class Solution:
    def countPrimes(self, n: int) -> int:
        arr=set()
        if n<=2:
            return 0
        for i in range(2,n):
            if i not in arr:
                for j in range(i,n//i+1):
                    if i*j<n:
                        arr.add(i*j)
        res=n-2-len(arr)
        return res