class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.upper()
        s=s.replace('-','')
        res=[]
        if len(s)%k:
            res.append(s[:len(s)%k])
            s=s[len(s)%k:]
        for i in range(0,len(s)-k+1,k):
            res.append(s[i:i+k])
        return '-'.join(res)