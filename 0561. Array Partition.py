class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums) // 2
        nums.sort()
        res = 0
        for i in range(n):
            res += nums[2 * i]
        return res

