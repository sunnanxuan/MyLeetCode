class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums=list(map(str,nums))
        if len(nums)>=3:
            nums[1]='('+nums[1]
            nums[-1]=nums[-1]+')'
        return '/'.join(nums)