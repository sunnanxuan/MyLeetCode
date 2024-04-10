class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        r=m
        c=n
        for i,j in ops:
            r=min(r,i)
            c=min(c,j)
        return r*c