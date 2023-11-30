class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        while l<r:
            res=max(res,(r-l)*min(height[r],height[l]))
            if height[r]<=height[l]:
                r-=1
            elif height[r]>height[l]:
                l+=1
        return res