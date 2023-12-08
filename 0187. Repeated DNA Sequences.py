class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)
        res=[]
        for i in range(n-10):
            if s[i:i+10] not in res and s[i:i+10] in s[i+1:]:
                res.append(s[i:i+10])
        return res