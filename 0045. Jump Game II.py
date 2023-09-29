class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[[float('inf'),0] for _ in range(len(nums))]
        dp[0]=[0,nums[0]]
        for i in range(len(nums)):
            for j in range(i+1,min(len(nums),i+dp[i][1]+1)):
                if dp[j][0]>dp[i][0]+1:
                    dp[j]=[dp[i][0]+1,nums[j]]
        return dp[-1][0]