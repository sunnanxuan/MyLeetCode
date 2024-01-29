class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res=0
        if len(points)==1:
            return 1
        for i,j in points:
            slope=collections.defaultdict(int)
            for x,y in points:
                if x==i and y==j:
                    continue
                elif x==i:
                    slope['*']+=1
                else:
                    slope[(y-j)/(x-i)]+=1
            res=max(res,max(slope.values())+1)
        return res