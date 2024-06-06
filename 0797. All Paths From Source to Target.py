class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        def path(i):
            res=[]
            for j in graph[i]:
                tail=path(j)
                for t in tail:
                    if t[-1]==n-1:
                        res.append([i]+t)
            if not res and i==n-1:return [[i]]
            else:return res

        res=[]
        res.extend(path(0))
        return res