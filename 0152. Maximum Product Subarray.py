class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp=[[0,0,0] for i in range(len(nums))]
        dp[0]=[nums[0],nums[0],nums[0]]
        for i in range(1,len(nums)):
            dp[i][0]=max(nums[i],nums[i]*dp[i-1][0],nums[i]*dp[i-1][1])
            dp[i][1]=min(nums[i],nums[i]*dp[i-1][0],nums[i]*dp[i-1][1])
            dp[i][2]=max(dp[i][0],dp[i-1][2])
        return dp[-1][2]