class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        stack=[]
        l=len(nums2)
        for n in nums2[::-1]:
            while stack and stack[-1]<=n:
                stack.pop()
            if not stack:
                dic[n]=-1
            else:
                dic[n]=stack[-1]
            stack.append(n)
        res=[]
        for n1 in nums1:
            res.append(dic[n1])
        return res