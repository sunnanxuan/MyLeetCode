class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=collections.Counter(tasks)
        lst=sorted(list(count.values()))
        res=0
        c=lst.pop()
        res+=c
        p=c-1
        while lst:
            m=lst.pop()
            if n>0:
                if m==c:
                    n-=1
                    res+=m
                else:
                    if p>=m:p-=m
                    else:
                        n-=1
                        p=c-1-(m-p)
                    res+=m
            else:res+=m
        if n>0:res+=(c-1)*(n-1)+p
        return res