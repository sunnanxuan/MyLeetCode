class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic=collections.Counter(nums)
        return [k for k in dic if dic[k]==1]