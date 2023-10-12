class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d=False
        i=1
        while i<len(nums):
            if not d and nums[i]==nums[i-1]:
                d=True
                i+=1
            elif d and nums[i]==nums[i-1]:
                nums.pop(i)
            elif nums[i]!=nums[i-1]:
                d=False
                i+=1
        return len(nums)