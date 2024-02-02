class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp=[[1,1] for _ in range(len(nums))]
        res=1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i][0]=max(dp[i][0],1+dp[j][1])
                elif nums[i]<nums[j]:
                    dp[i][1]=max(dp[i][1],1+dp[j][0])
            res=max(res,max(dp[i]))
        return res