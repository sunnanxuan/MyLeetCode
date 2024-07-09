class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        dic=collections.defaultdict(set)
        for a,b in richer:
            dic[b].add(a)
        memo={}
        def find(c):
            if c in memo:
                return memo[c]
            elif c not in dic:return [c,quiet[c]]
            else:
                cur=[c,quiet[c]]
                for n in dic[c]:
                    m=find(n)
                    cur=min([cur,m],key=lambda x:x[1])
                memo[c]=cur
                return memo[c]
        res=[]
        for i in range(len(quiet)):
            r=find(i)
            res.append(r[0])
        return res
