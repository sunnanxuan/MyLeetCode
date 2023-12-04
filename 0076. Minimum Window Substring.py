class Solution:
    def minWindow(self, s: str, t: str) -> str:
        diff=collections.Counter(t)
        res=[float('inf'),'']
        l=0
        r=1
        string=s[0]
        if s[0] in diff:
            diff[s[0]]-=1
        while l<len(s) and r<=len(s):
            if all(v<=0 for v in diff.values()):
                if r-l<res[0]:
                    res=[r-l,string]
                c=string[0]
                if c in diff:
                    diff[c]+=1
                string=string[1:]
                l+=1
            else:
                if r<len(s):
                    string+=s[r]
                    if s[r] in diff:
                        diff[s[r]]-=1
                r+=1
        return res[1]
