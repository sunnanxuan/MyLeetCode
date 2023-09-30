class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=set(itertools.permutations(nums,len(nums)))
        return res
