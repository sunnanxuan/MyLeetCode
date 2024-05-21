class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack=[]
        i=0
        n=len(formula)
        while i<n:
            c=formula[i]
            if c.isupper():
                i+=1
                while i<n and formula[i].islower():
                    c+=formula[i]
                    i+=1
                stack.append([c,1])
            elif c.isdigit():
                j=i+1
                if j<n and formula[j].isdigit():
                    c+=formula[j]
                    j+=1
                i=j
                if stack[-1]==')':
                    arr=[]
                    stack.pop()
                    while stack[-1]!='(':
                        s,m=stack.pop()
                        arr.append([s,m*int(c)])
                    stack.pop()
                    arr.reverse()
                    stack.extend(arr)
                else:stack[-1][1]*=int(c)
            elif c=='(' or c==')':
                stack.append(c)
                i+=1
        dic=collections.defaultdict(int)
        for p in stack:
            if p!='(' and p!=')':s,m=p;dic[s]+=m
        res=[]
        for k,v in sorted(dic.items()):
            res.append(k)
            if v>1:res.append(str(v))
        return ''.join(res)