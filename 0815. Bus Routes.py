class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dic=collections.defaultdict(set)
        for i,r in enumerate(routes):
            for b in r:
                dic[b].add(i)
        visited=set()
        q={source}
        res=0
        while q:
            if target in q:return res
            new=set()
            for c in q:
                for j in dic[c]:
                    if j not in visited:
                        visited.add(j)
                        for s in routes[j]:
                            new.add(s)
            res+=1
            q=new
        return -1