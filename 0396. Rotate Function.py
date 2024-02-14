class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        for i in range(n):
            res+=i*nums[i]
        sm=sum(nums)
        cur=res
        for j in range(n-1):
            cur-=sm
            cur+=(n*nums[j])
            res=max(res,cur)
        return res
