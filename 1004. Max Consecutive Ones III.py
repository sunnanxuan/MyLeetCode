class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        zeros = [-1]
        for i, n in enumerate(nums):
            if n == 0:
                zeros.append(i)
        zeros.append(len(nums))
        if len(zeros) - 2 <= k: return len(nums)
        sm = 0
        for i in range(k + 1):
            sm += zeros[1 + i] - zeros[0 + i]
        sm -= 1
        res = sm
        for i in range(k + 1, len(zeros) - 1):
            sm -= zeros[i - k] - zeros[i - k - 1]
            sm += zeros[i + 1] - zeros[i]
            res = max(res, sm)
        return res
