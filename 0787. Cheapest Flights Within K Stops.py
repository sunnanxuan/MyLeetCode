class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dic=collections.defaultdict(list)
        for s,d,v in flights:
            dic[s].append((d,v))
        memo={}
        def fly(k,cur):
            if k<0:return -1
            elif (k,cur) in memo:return memo[(k,cur)]
            elif cur==dst:
                memo[(k,cur)]=0
                return 0
            else:
                lst=[]
                for d,v in dic[cur]:
                    m=fly(k-1,d)
                    if m!=-1:
                        lst.append(v+m)
                if not lst:res=-1
                else:res=min(lst)
                memo[(k,cur)]=res
                return res

        res=fly(k+1,src)
        return res