class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic12 = collections.defaultdict(int)
        dic34 = collections.defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                dic12[n1 + n2] += 1
        for n3 in nums3:
            for n4 in nums4:
                dic34[n3 + n4] += 1
        res = 0
        for k in dic12:
            if 0 - k in dic34:
                res += dic12[k] * dic34[0 - k]
        return res
