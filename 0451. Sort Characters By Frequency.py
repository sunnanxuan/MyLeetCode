class Solution:
    def frequencySort(self, s: str) -> str:
        dic=collections.Counter(s)
        count=list(dic.items())
        count.sort(key=lambda x:(-1*x[1],x[0]))
        res=[]
        for c,n in count:
            res.append(c*n)
        return ''.join(res)
