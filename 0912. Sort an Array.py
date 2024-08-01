class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:return nums
        else:
            res=[]
            n=len(nums)
            left=nums[:n//2]
            right=nums[n//2:]
            l=self.sortArray(left)
            r=self.sortArray(right)
            while l and r:
                if l[0]<=r[0]:res.append(l.pop(0))
                else:res.append(r.pop(0))
            if l:res.extend(l)
            elif r:res.extend(r)
            return res
