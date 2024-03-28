class Solution:
    def checkRecord(self, s: str) -> bool:
        a=0
        l=0
        pre=0
        for c in s:
            if c=='A':
                pre=0
                a+=1
                if a>=2:
                    return False
            elif c=='L':
                pre+=1
                if pre>=3:
                    return False
            else:
                pre=0
        return True