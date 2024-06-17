class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal=set()
        rem=set()
        dic={}
        for i in range(len(graph)):
            if not graph[i]:
                rem.add(i)
                terminal.add(i)
            else:dic[i]=set(graph[i])
        while rem:
            rem=set()
            for k in dic:
                if not dic[k]-terminal:
                    terminal.add(k)
                    rem.add(k)
            for k in rem:dic.pop(k)
        return sorted(list(terminal))