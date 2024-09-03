class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        n = len(nums)
        for i in range(n - 1, 1, -1):
            if nums[i] * 3 <= res: break
            for j in range(i - 1, 0, -1):
                if nums[j - 1] > nums[i] - nums[j]:
                    res = max(res, nums[j - 1] + nums[i] + nums[j])
                    break
        return res
