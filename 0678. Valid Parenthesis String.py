class Solution:
    def checkValidString(self, s: str) -> bool:
        l=stars=0
        for c in s:
            if c=='(':
                l+=1
            elif c=='*':
                stars+=1
            elif c==')':
                if l>0:l-=1
                elif stars>0:stars-=1
                else:return False
        if l>stars:return False
        r=stars=0
        for c in s[::-1]:
            if c==')':
                r+=1
            elif c=='*':
                stars+=1
            elif c=='(':
                if r>0:r-=1
                elif stars>0:stars-=1
                else:return False
        if r>stars:return False
        return True