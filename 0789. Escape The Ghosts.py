class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dt=abs(target[0])+abs(target[1])
        dg=float('inf')
        for x,y in ghosts:
            dg=min(dg,abs(target[0]-x)+abs(target[1]-y))
        return dt<dg