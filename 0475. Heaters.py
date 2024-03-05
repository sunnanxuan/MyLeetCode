class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        res=0
        for h in houses:
            p=bisect.bisect(heaters,h)
            if p==0:
                n=heaters[0]-h
            elif p==len(heaters):
                n=h-heaters[-1]
            else:
                n=min(h-heaters[p-1],heaters[p]-h)
            res=max(n,res)
        return res