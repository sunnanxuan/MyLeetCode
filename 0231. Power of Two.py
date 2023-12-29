class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      m=1
      while m<n:
        m<<=1
      return m==n