class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        inds=collections.defaultdict(list)
        for i,c in enumerate(s):
            if len(inds[c])<=1:inds[c].append(i)
            else:
                inds[c].pop()
                inds[c].append(i)
        p=-1
        res=[]
        l=0
        while l<len(s):
            if len(inds[s[l]])==1:
                res.append((l-p))
                p=l
                l+=1
            else:
                j=l+1
                r=inds[s[l]][1]
                while j<r:
                    r=max(inds[s[j]][-1],r)
                    j+=1
                res.append((j-p))
                p=j
                l=j+1
        return res