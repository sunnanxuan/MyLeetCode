class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=sorted(nums1+nums2)
        l=len(nums)
        if l%2==1:
            return nums[l//2]
        else:
            return (nums[l//2-1]+nums[l//2])/2