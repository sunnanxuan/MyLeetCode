class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
      dic=collections.Counter(nums)
      n=len(nums)
      return [k for k in dic if dic[k]>n/3]