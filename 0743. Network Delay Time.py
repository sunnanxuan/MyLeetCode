class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited={}
        dic=collections.defaultdict(list)
        for s,v,w in times:
            dic[s].append((v,w))
        visited[k]=0
        q=[(k,0)]
        while q:
            new=[]
            for node,t in q:
                for v,w in dic[node]:
                    if v not in visited or t+w<visited[v]:
                        new.append((v,t+w))
                        visited[v]=t+w
            q=new
        if len(visited)<n:return -1
        else:return max(visited.values())