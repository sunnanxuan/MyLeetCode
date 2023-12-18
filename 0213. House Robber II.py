class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
          return max(nums)
        dp1=[0]*(len(nums)-1)
        dp2=[0]*(len(nums)-1)
        dp1[0]=nums[0]
        dp1[1]=nums[1]
        dp1[2]=nums[2]+nums[0]
        dp2[0]=nums[1]
        dp2[1]=nums[2]
        dp2[2]=nums[3]+nums[1]
        for i in range(3,len(nums)-1):
          dp1[i]=nums[i]+max(dp1[i-2],dp1[i-3])
          dp2[i]=nums[i+1]+max(dp2[i-2],dp2[i-3])
        return max(dp1[-1],dp1[-2],dp2[-1],dp2[-2])