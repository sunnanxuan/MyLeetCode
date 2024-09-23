class Solution:
    def bitwiseComplement(self, n: int) -> int:
        m=bin(n)[2:]
        new=[]
        for c in m:
            if c=='0':new.append('1')
            else:new.append('0')
        return int(''.join(new),2)