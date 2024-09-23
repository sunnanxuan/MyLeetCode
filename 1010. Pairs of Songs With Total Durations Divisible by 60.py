class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic=collections.defaultdict(int)
        res=0
        for t in time:
            rem=t%60
            res+=dic[(60-rem)%60]
            dic[rem]+=1
        return res
