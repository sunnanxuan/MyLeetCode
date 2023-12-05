class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=[]
        while columnNumber:
            n=columnNumber%26
            columnNumber//=26
            if n==0:
                columnNumber-=1
                res.append('Z')
            else:
                res.append(chr(n+64))
        return ''.join(res[::-1])