class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):return False
        if s==goal and len(s)>len(set(s)):return True
        dic_s={}
        dic_g={}
        for i in range(len(s)):
            if s[i]==goal[i]:continue
            else:
                dic_s[i]=s[i]
                dic_g[i]=goal[i]
        if len(dic_s)!=2:
            return False
        i,j =dic_s.keys()
        if dic_s[i]==dic_g[j] and dic_s[j]==dic_g[i]:
            return True
        else:return False