class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        def Palindrome(l,r,d):
            if l>=r:return True
            elif s[l]==s[r]:
                return Palindrome(l+1,r-1,d)
            else:
                if d==1:
                    return False
                elif d==0:
                    return Palindrome(l+1,r,1) or Palindrome(l,r-1,1)
        return Palindrome(l,r,0)