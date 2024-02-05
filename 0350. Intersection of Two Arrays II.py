class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = collections.Counter(nums1)
        res = []
        for n in nums2:
            if dic[n]:
                res.append(n)
                dic[n] -= 1
        return res
