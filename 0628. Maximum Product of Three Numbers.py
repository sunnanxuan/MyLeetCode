class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l=len(nums)
        res=-float('inf')
        if len(nums)==3:
            res=nums[0]*nums[1]*nums[2]
        elif len(nums)>=4:
            ll=nums[0]*nums[1]
            rr=nums[-1]*nums[-2]
            lr=nums[0]*nums[-1]
            for i,n in enumerate(nums):
                if i==0:
                    res=max(res,n*nums[2]*nums[1],n*nums[-1]*nums[1],n*rr)
                elif i==1:
                    res=max(res,n*lr,n*rr)
                elif i==(l-2):
                    res=max(res,n*nums[-1]*nums[-3],n*ll,n*lr)
                elif i==(l-1):
                    res=max(res,n*nums[-2]*nums[-3],n*ll,n*nums[-2]*nums[0])
                else:
                    res=max(res,n*ll,n*rr,n*lr)
        return res