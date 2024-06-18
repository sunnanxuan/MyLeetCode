class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic=collections.defaultdict(int)
        for cp in cpdomains:
            cp=cp.split()
            n,c=cp
            c=c.split('.')
            for i in range(len(c)):
                s='.'.join(c[i:])
                dic[s]+=int(n)
        res=[str(dic[k])+' '+k for k in dic]
        return res