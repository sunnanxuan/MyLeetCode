class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        renums=list(reversed(nums))
        dic=collections.Counter(nums)
        res=n=len(nums)
        m=max(dic.values())
        arr=[k for k in dic if dic[k]==m]
        for num in arr:
            l=n-nums.index(num)-renums.index(num)
            res=min(res,l)
        return res