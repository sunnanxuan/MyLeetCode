class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]
        count=collections.defaultdict(int)
        inds=collections.defaultdict(list)
        dic={}
        for log in logs:
            m,op,t=log.split(':')
            if op=='end':
                if stack[-1]==m:
                    count[m]+=(int(t)-dic[stack[-1]]+1)
                    ind=inds[m].pop()
                    stack.pop(ind)
                    dic.pop(m)
                    if stack:
                        p=stack[-1]
                        dic[p]=int(t)+1
                else:
                    ind=inds[m].pop()
                    stack.pop(ind)
                    dic.pop(m)

            else:
                if stack:
                    p=stack[-1]
                    count[p]+=(int(t)-dic[p])
                stack.append(m)
                inds[m].append(len(stack)-1)
                dic[m]=int(t)
        res=[]
        for i in range(n):
            res.append(count[str(i)])
        return res