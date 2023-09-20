class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l=j+1
                r=len(nums)-1
                while l<r:
                    sm=nums[i]+nums[j]+nums[l]+nums[r]
                    if sm==target:
                        res.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                        r-=1
                    elif sm<target:
                        l+=1
                    elif sm>target:
                        r-=1
        return res