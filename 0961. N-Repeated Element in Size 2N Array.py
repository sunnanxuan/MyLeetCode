class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic=collections.Counter(nums)
        return max(dic.items(),key=lambda x:x[1])[0]