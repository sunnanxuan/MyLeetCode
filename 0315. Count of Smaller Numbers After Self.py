class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        arr=[nums[-1]]
        for i in range(-2,-1*(len(nums)+1),-1):
            p=bisect.bisect_left(arr,nums[i])
            res[i]=p
            bisect.insort(arr,nums[i])
        return res