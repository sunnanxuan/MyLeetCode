class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=1
        sm=nums[0]
        res=float('inf')
        while i<len(nums):
            if sm<target and j<len(nums):
                sm+=nums[j]
                j+=1
            elif sm>=target:
                res=min(res,j-i)
                sm-=nums[i]
                i+=1
            else:
                break
        if res==float('inf'):
            return 0
        else:
            return res