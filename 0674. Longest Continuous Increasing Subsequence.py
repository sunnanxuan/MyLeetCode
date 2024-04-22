class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res=0
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums) and nums[j-1]<nums[j]:
                j+=1
            res=max(res,j-i)
            i=j
        return res