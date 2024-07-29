class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        l=bin(left)[2:]
        r=bin(right)[2:]
        if len(r)>len(l):return 0
        else:
            res=[]
            i=0
            while i<len(l) and l[i]==r[i]:
                res.append(l[i])
                i+=1
            while i<len(l):
                res.append('0')
                i+=1
            return int(''.join(res),2)
