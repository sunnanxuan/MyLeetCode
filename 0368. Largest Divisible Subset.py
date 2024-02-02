class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[0, []] for _ in range(len(nums))]
        dp[0] = [1, [nums[0]]]
        for i in range(1, len(nums)):
            dp[i] = [1, [nums[i]]]
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1 + dp[j][0] > dp[i][0]:
                    dp[i][0] = 1 + dp[j][0]
                    dp[i][1] = dp[j][1] + [nums[i]]
        return max(dp)[1]
