class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=2
        l=len(s)
        while n<=l:
            if l%n==0:
                if s[:l//n]*n==s:
                    return True
            n+=1
        return False