class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        dic=collections.defaultdict(int)
        t=collections.defaultdict(int)
        d=collections.defaultdict(int)
        for i in range(len(tops)):
            if tops[i]==bottoms[i]:dic[tops[i]]+=1
            else:
                dic[tops[i]]+=1
                dic[bottoms[i]]+=1
            t[tops[i]]+=1
            d[bottoms[i]]+=1
        if max(dic.values())<len(tops):return -1
        k=sorted(list(dic.items()),key=lambda x:x[1])[-1][0]
        return len(tops)-max(t[k],d[k])