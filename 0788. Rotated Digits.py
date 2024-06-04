class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid={'0','1','2','5','6','8','9'}
        same={'0','1','8'}
        res=0
        for i in range(1,n+1):
            c=set(str(i))
            if not c-valid and c-same:res+=1
        return res