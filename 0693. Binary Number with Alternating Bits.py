class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s=bin(n)[2:]
        pre='#'
        for i in range(len(s)):
            if s[i]==pre:return False
            else:
                pre=s[i]
        return True