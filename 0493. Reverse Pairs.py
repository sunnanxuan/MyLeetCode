class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res=0
        stack=[]
        for n in nums:
            p=bisect.bisect_right(stack,2*n)
            res+=(len(stack)-p)
            bisect.insort(stack,n)
        return res