class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic=collections.Counter(nums)
        res=0
        nums=set(nums)
        for n in nums:
            if n-1 in dic:
                res=max(res,dic[n]+dic[n-1])
            if n+1 in dic:
                res=max(res,dic[n]+dic[n+1])
        return res