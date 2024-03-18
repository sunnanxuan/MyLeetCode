class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        sm=sum(machines)
        n=len(machines)
        if sm%n:
            return -1
        m=sm//n
        move=list(map(lambda x:x[0]-x[1] , zip(machines,[m]*n)))
        res=0
        cur=0
        for c in move:
            cur+=c
            res=max(res,abs(cur),c)
        return res