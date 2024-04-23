class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res=[]
        dic=collections.defaultdict(set)
        for s,e in edges:
            if s not in dic[e] or e not in dic[s]:
                dic[s].add(e)
                dic[s]|=dic[e]
                for c in dic[s]:
                    dic[c].add(e)
                    dic[c]|=dic[e]
                dic[e].add(s)
                dic[e]|=dic[s]
                for c in dic[e]:
                    dic[c].add(s)
                    dic[c]|=dic[s]
            else:
                res.append([s,e])

        return res and res[-1] or []
