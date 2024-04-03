class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited=set()
        res=0
        for n in nums:
            if n not in visited:
                visited.add(n)
                c=1
                m=nums[n]
                while m not in visited:
                    c+=1
                    visited.add(m)
                    m=nums[m]
                res=max(res,c)
        return res