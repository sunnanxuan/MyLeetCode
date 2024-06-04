class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic=collections.Counter(s)
        res=[]
        for c in order:
            if c in dic:
                res.append(c*dic[c])
                dic.pop(c)
        for k in dic:
            res.append(k*dic[k])
        return ''.join(res)