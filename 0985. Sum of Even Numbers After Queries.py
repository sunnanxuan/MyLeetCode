class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        sm=sum([nums[i] for i in range(len(nums)) if nums[i]%2==0])
        for v,i in queries:
            if nums[i]%2==0:
                if v%2==0:sm+=v
                else:sm-=nums[i]
            else:
                if v%2!=0:sm+=(nums[i]+v)
            nums[i]+=v
            res.append(sm)
        return res
