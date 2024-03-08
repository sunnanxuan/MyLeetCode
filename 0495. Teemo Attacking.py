class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        pre=-1
        res=0
        for t in timeSeries:
            if pre>=0 and t>pre+duration-1:
                res+=duration
            elif pre>=0 and t<=pre+duration-1:
                res+=(t-pre)
            pre=t
        res+=duration
        return res