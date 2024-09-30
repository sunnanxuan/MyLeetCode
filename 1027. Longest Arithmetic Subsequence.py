class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        minv, maxv = min(nums), max(nums)
        diff = maxv - minv
        ans = 1

        for d in range(-diff, diff + 1):
            f = dict()
            for num in nums:
                if (prev := num - d) in f:
                    f[num] = max(f.get(num, 0), f[prev] + 1)
                    ans = max(ans, f[num])
                f[num] = max(f.get(num, 0), 1)

        return ans
