class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q=[['',0,0]]
        res=[]
        while q:
            new=[]
            for s,l,r in q:
                if l<n:
                    new.append([s+'(',l+1,r])
                if r<l:
                    if r+1==l==n:
                        res.append(s+')')
                    else:
                        new.append([s+')',l,r+1])
            q=new
        return res