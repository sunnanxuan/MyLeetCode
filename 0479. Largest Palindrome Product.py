class Solution:
    def largestPalindrome(self, n: int) -> int:
        mod=1337
        def divide(m):
            d=10**n-1
            while m//d<=d:
                if m//d*d==m:
                    return True
                else:
                    d-=1
            return False
        if n==1:
            return 9
        l=10**n-1
        while l:
            m=int(str(l)+str(l)[::-1])
            if divide(m):
                break
            else:
                l-=1
        return m%mod