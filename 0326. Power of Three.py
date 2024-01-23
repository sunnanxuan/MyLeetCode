class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            cur = 1
            while cur < n:
                cur *= 3
            return cur == n
