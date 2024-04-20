class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:-1*x[0])
        ls=[-1*p[0] for p in pairs]
        dic={}
        dic[-1]=0
        cur=0
        for i in range(len(pairs)):
            r=pairs[i][1]
            ind=bisect.bisect_left(ls,-1*r)
            cur=max(cur,dic[ind-1]+1)
            dic[i]=cur
        return max(dic.values())