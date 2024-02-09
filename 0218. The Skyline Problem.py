class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points=[]
        ends=collections.defaultdict(list)
        for s,e,h in buildings:
            points.append([s,h])
            if [e,0] not in points:
                points.append([e,0])
            ends[e].append(h)
        points.sort(key=lambda x:(x[0],-1*x[1]))
        res=[]
        heights=[]
        cur=0
        for p,h in points:
            if not heights:
                res.append([p,h])
                heights.append(h)
                cur=h
            elif h==0:
                for m in ends[p]:
                    heights.remove(m)
                if not heights:
                    cur=0
                    res.append([p,0])

                elif max(heights)<cur:
                    cur=max(heights)
                    res.append([p,cur])
            else:
                if h>cur:
                    res.append([p,h])
                    cur=h
                heights.append(h)
        return res