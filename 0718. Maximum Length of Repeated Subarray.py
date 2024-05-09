class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        dp=[0]*(n2+1)
        res=0
        for i in range(1,n1+1):
            new=[0]*(n2+1)
            for j in range(1,n2+1):
                if nums1[i-1]!=nums2[j-1]:
                    continue
                else:
                    new[j]=dp[j-1]+1
            res=max(res,max(new))
            dp=new
        return res