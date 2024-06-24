class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res=0
        ages.sort()
        lst=[2*(c-7) for c in ages]
        for i in range(len(ages)):
            p1=bisect.bisect_right(ages,ages[i])-1
            p2=bisect.bisect_right(lst,ages[i])
            if ages[i]<100:
                p3=bisect.bisect_right(ages,100)
            else:p3=len(ages)
            n=min(p1,p3)-p2
            res+=max(0,n)
        return res