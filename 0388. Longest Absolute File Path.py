class Solution:
    def lengthLongestPath(self, input: str) -> int:
        inp=input.split("\n")
        res=0
        stack=[]
        for c in inp:
            s=c.lstrip('\t')
            n=len(c)-len(s)
            while stack and stack[-1][1]>=n:
                stack.pop()
            stack.append([s,n,len(s)])
            if '.' in s:
                m=0
                for _,_,l in stack:
                    m+=(l+1)
                res=max(res,m-1)
        return res