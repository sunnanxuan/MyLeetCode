class Solution:
    def countAndSay(self, n: int) -> str:
        s='1'
        for i in range(2,n+1):
            count=1
            n=[]
            for j in range(1,len(s)):
                if s[j]==s[j-1]:
                    count+=1
                else:
                    n.append(str(count)+s[j-1])
                    count=1
            n.append(str(count)+s[-1])
            s=''.join(n)
        return s