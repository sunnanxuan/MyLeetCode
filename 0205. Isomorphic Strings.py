class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic_s={}
        dic_t={}
        for i in range(len(s)):
            if (s[i] not in dic_s)+(t[i] not in dic_t)==2:
                dic_s[s[i]]=t[i]
                dic_t[t[i]]=s[i]
            elif (s[i] not in dic_s)+(t[i] not in dic_t)==1:
                return False
            elif dic_s[s[i]]==t[i] and dic_t[t[i]]==s[i]:
                continue
            else:
                return False
        return True