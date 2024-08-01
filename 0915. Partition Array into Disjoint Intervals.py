class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        mxl=[0]*len(nums)
        mnr=[0]*len(nums)
        ml=-1*float('inf')
        mr=float('inf')
        for i in range(len(nums)):
            ml=max(ml,nums[i])
            mxl[i]=ml
            mr=min(mr,nums[-i-1])
            mnr[-i-1]=mr
        for i in range(len(nums)):
            if mxl[i]<=mnr[i+1]:return i+1