class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res=0
        tail=0
        for s,e in points:
            if res==0:
                res+=1
                tail=e
            else:
                if s<=tail:
                    tail=min(e,tail)
                else:
                    res+=1
                    tail=e
        return res