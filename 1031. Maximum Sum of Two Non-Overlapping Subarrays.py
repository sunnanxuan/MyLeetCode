class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:

        memo = {}

        def maxsum(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            elif secondLen > r - l:
                return float('-inf')
            else:
                sm = sum(nums[l:l + secondLen])
                res = sm
                for i in range(l + 1, r - secondLen + 1):
                    sm -= nums[i - 1]
                    sm += nums[i + secondLen - 1]
                    res = max(res, sm)
                memo[(l, r)] = res
                return memo[(l, r)]

        res = float('-inf')
        sm = sum(nums[:firstLen - 1]) + nums[-1]
        for i in range(len(nums) - firstLen + 1):
            sm -= nums[i - 1]
            sm += nums[i + firstLen - 1]
            res = max(res, sm + max(maxsum(0, i), maxsum(i + firstLen, len(nums))))
        return res











