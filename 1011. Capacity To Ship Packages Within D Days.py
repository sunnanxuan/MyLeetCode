class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def countdays(w):
            res=0
            i=0
            sm=0
            while i<len(weights):
                if sm+weights[i]<=w:
                    sm+=weights[i]
                else:
                    res+=1
                    sm=weights[i]
                i+=1
            res+=1
            return res

        l=max(math.ceil(sum(weights)/days),max(weights))
        r=sum(weights)
        while l<r:
            mid=(l+r)//2
            if countdays(mid)<=days:
                r=mid
            else:
                l=mid+1
        return l
