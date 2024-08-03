class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sm = sum(nums)
        mns = float('inf')
        mxs = -1 * float('inf')
        cur = 0
        l = r = 0
        while r < len(nums):
            while l < r and (nums[l] >= 0 or cur >= 0):
                cur -= nums[l]
                l += 1
            cur += nums[r]
            mns = min(mns, cur)
            r += 1
        cur = 0
        l = r = 0
        while r < len(nums):
            while l < r and (nums[l] <= 0 or cur < 0):
                cur -= nums[l]
                l += 1
            cur += nums[r]
            mxs = max(mxs, cur)
            r += 1
        if sm != mns:
            res = max(sm, mxs, sm - mns)
        else:
            res = mxs
        return res
