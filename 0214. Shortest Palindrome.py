class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        for i in range(1,len(s)):
            n=s[-i:][::-1]+s
            if n==n[::-1]:
                return n