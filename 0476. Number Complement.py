class Solution:
    def findComplement(self, num: int) -> int:
        res=[]
        for c in bin(num)[2:]:
            if c=='0':
                res.append('1')
            else:
                res.append('0')
        return int(''.join(res),2)