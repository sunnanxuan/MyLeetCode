class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        s1=sorted(s1)
        for i,c in enumerate(s2):
            if c in s1:
                if sorted(s2[i:i+n])==s1:
                    return True
        return False