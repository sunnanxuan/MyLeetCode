class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:return intervals
        p=[]
        for i in intervals:
            p.extend(i)
        l=bisect.bisect_left(p,newInterval[0])
        r=bisect.bisect_right(p,newInterval[1])
        if l==r:
            p[l:l]=newInterval*(l%2==0)
        else:
            if l%2==0:
                left=newInterval[0]
            else:
                left=p[l-1]
                l-=1
            if r%2==0:
                right=newInterval[1]
            else:
                right=p[r]
                r+=1
            p[l:r]=[left,right]
        res=[]
        for j in range(0,len(p),2):
            res.append([p[j],p[j+1]])
        return res
