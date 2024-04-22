class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp=[[1,1] for _ in range(len(nums))]
        for i in range(1,len(nums)):
            c=[1,1]
            for j in range(i):
                if nums[j]<nums[i]:
                    if dp[j][0]+1>c[0]:
                        c=[dp[j][0]+1,dp[j][1]]
                    elif dp[j][0]+1==c[0]:
                        c[1]+=dp[j][1]
            dp[i]=c
        m=max(dp)[0]
        res=sum([n[1] for n in dp if n[0]==m])
        return res
