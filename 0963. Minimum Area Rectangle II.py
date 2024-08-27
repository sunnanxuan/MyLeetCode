class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        res=float('inf')
        for each in itertools.combinations(points,4):
            each=sorted(each)
            a,b,c,d=each
            l1=(a[0]-b[0])**2+(a[1]-b[1])**2
            l2=(a[0]-c[0])**2+(a[1]-c[1])**2
            m=(b[0]-c[0])**2+(b[1]-c[1])**2
            r1=(d[0]-b[0])**2+(d[1]-b[1])**2
            r2=(d[0]-c[0])**2+(d[1]-c[1])**2
            if l1+l2==m and r1+r2==m and l1==r2:
                s=(l1*l2)**0.5
                res=min(res,s)
        if res==float('inf'):return 0
        else:return res

