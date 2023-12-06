class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=collections.Counter(nums)
        lst=list(dic.items())
        lst.sort(key=lambda x:x[1])
        return lst[-1][0]