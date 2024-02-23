class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic=collections.Counter(p)
        cur=collections.Counter(s[:len(p)])
        res=[]
        if dic==cur:
            res.append(0)
        for i in range(1,len(s)-len(p)+1):
            c=s[i+len(p)-1]
            if c not in cur:
                cur[c]=1
            else:
                cur[c]+=1
            cur[s[i-1]]-=1
            if cur[s[i-1]]==0:
                cur.pop(s[i-1])
            if cur==dic:
                res.append(i)
        return res
