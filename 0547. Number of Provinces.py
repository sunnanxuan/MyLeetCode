class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dic=collections.defaultdict(set)
        for i,c in enumerate(isConnected):
            dic[i].add(i)
            con=[]
            for j in range(len(c)):
                if c[j]==1:
                    dic[i].add(j)
                    con.extend(list(dic[j]-dic[i]))
                    dic[i]|=dic[j]
            while con:
                new=[]
                for k in con:
                    new.extend(list(dic[k]-dic[i]))
                    dic[i]|=dic[k]
                con=new
        p=[n for n in range(len(isConnected))]
        res=0
        while p:
            cur=p.pop()
            res+=1
            for v in dic[cur]:
                if v in p:p.remove(v)
        return res
