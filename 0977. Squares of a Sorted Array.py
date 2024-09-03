class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = sorted([n ** 2 for n in nums])
        return res
