class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sm=sum(nums[:k])
        res=sm
        for i in range(len(nums)-k):
            sm-=nums[i]
            sm+=nums[i+k]
            res=max(res,sm)
        return res/k
