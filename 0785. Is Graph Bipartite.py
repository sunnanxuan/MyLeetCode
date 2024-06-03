class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        g={u:graph[u] for u in range(len(graph))}
        nums={u for u in range(len(graph))}
        q=[]
        l=set()
        r=set()
        while not q and nums:
            m=min(nums)
            q.append(m)
            l.add(m)
            while q:
                new=[]
                for u in q:
                    nums.discard(u)
                    for v in g[u]:
                        if v in nums:
                            if v in l:return False
                            else:
                                r.add(v)
                                new.append(v)
                q=new
                r,l=l,r
        return True