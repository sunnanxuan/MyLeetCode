class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for n in range(left,right+1):
            for c in str(n):
                if c=='0' or n%int(c):
                    break
            else:
                res.append(n)
        return res
