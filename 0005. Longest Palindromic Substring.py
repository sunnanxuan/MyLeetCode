class Solution:
    def longestPalindrome(self, s: str) -> str:
        def Palindrome(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return [r-l-1,s[l+1:r]]
        res=s[0]
        ml=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                even=Palindrome(i-2,i+1)
                if even[0]>ml:
                    res=even[1]
                    ml=even[0]
            odd=Palindrome(i-1,i+1)
            if odd[0]>ml:
                res=odd[1]
                ml=odd[0]
        return res