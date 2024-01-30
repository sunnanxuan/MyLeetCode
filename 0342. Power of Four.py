class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        cur=1
        while cur<n:
            cur*=4
        return cur==n