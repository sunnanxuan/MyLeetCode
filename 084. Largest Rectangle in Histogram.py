class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights=heights+[0]
        res=0
        stack=[[0,-1]]
        for i,h in enumerate(heights):
            if h>=stack[-1][0]:
                stack.append([h,i])
            else:
                while stack[-1][0]>h:
                    cur=stack.pop()[0]
                    res=max(res,cur*(i-stack[-1][1]-1))
                stack.append([h,i])
        return res
