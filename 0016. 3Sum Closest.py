class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=[0,-float('inf')]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                sm=nums[i]+nums[l]+nums[r]
                if abs(sm-target)<=abs(res[1]):
                    res=[sm,sm-target]
                    if res[1]==0:return sm
                if sm<target:
                    l+=1
                elif sm>target:
                    r-=1
        return res[0]

