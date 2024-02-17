class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        diff=nums[1]-nums[0]
        n=2
        res=0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]==diff:
                n+=1
            else:
                res+=((1+(n-2))*(n-2)//2)
                n=2
                diff=nums[i]-nums[i-1]
        res+=((1+(n-2))*(n-2)//2)
        return res