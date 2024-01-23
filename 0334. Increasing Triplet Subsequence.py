class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3:
            return False
        mn = float('inf')
        secmin = float('inf')
        for n in nums:
            if n < mn:
                mn = n
            elif mn < n < secmin:
                secmin = n
            elif n > secmin:
                return True
        return False
