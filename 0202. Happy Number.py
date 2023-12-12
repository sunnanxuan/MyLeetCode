class Solution:
    def isHappy(self, n: int) -> bool:
        used=set()
        while n!=1:
            used.add(n)
            new=0
            while n>0:
                new+=(n%10)**2
                n//=10
            n=new
            if n in used:
                return False
        return True
