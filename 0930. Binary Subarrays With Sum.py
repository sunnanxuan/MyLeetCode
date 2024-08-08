class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res=0
        pre=1
        arr=[]
        l=0
        while l<len(nums):
            if nums[l]==0:
                pre+=1
                l+=1
            else:
                if goal==0:
                    res+=(pre-1)*pre//2
                r=l+1
                while r<len(nums) and nums[r]==0:
                    r+=1
                arr.append([pre,r-l])
                pre=r-l
                l=r
        if goal==0:
            res+=(pre-1)*pre//2
        else:
            for i in range(len(arr)-goal+1):
                res+=(arr[i][0]*arr[i+goal-1][1])
        return res

