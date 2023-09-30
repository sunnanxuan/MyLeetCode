class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list(itertools.permutations(nums, len(nums)))
        return res

