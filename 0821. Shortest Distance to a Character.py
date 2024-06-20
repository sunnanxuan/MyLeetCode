class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        inds=[]
        for i in range(len(s)):
            if s[i]==c:
                inds.append(i)
        res=[]
        for i in range(len(s)):
            p=bisect.bisect(inds,i)
            if p==0:res.append(inds[p]-i)
            elif p==len(inds):res.append(i-inds[p-1])
            else:res.append(min(inds[p]-i,i-inds[p-1]))
        return res