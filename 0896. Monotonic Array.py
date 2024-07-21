class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i=0
        while i+1<len(nums) and nums[i+1]==nums[i]:
            i+=1
        if i+1==len(nums):return True
        d=nums[i+1]-nums[i]
        i+=1
        for j in range(i,len(nums)-1):
            if d*(nums[j+1]-nums[j])>=0:
                continue
            else:
                return False
        return True
