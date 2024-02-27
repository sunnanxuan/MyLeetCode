class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums=sorted(list(set(nums)))
        cur=1
        res=[]
        for num in nums:
            while num>cur:
                res.append(cur)
                cur+=1
            cur+=1
        while cur<=n:
            res.append(cur)
            cur+=1
        return res