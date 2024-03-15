class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=sorted(score,reverse=True)
        dic={}
        for i in range(len(s)):
            if i==0:
                dic[s[i]]="Gold Medal"
            elif i==1:
                dic[s[i]]="Silver Medal"
            elif i==2:
                dic[s[i]]="Bronze Medal"
            else:
                dic[s[i]]=str(i+1)
        res=[]
        for c in score:
            res.append(dic[c])
        return res