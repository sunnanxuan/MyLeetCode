class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s)<=numRows:return s
        dic=collections.defaultdict(list)
        l=len(s)
        n=0
        i=0
        while i<l:
            if n==0:
                while i<l and n<numRows:
                    dic[n].append(s[i])
                    i+=1
                    n+=1
            if n==numRows:
                n-=2
                while i<l and n>0:
                    dic[n].append(s[i])
                    i+=1
                    n-=1
        res=[]
        for j in range(numRows):
            res.extend(dic[j])
        return "".join(res)


