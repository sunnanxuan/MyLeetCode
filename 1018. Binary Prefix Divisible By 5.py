class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        pre = 0
        res = []
        for n in nums:
            cur = pre * 2 + n
            res.append(bool(not cur % 5))
            pre = cur
        return res
