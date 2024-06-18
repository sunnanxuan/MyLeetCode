class Solution:
    def soupServings(self, n: int) -> float:
        memo={}
        def servesoup(A,B):
            if (A,B) in memo:return memo[(A,B)]
            if A<=0:
                if B>0:return 1
                else:return 0.5
            elif B<=0:return 0
            else:
                memo[(A,B)]=0.25*(servesoup(A-100,B)+servesoup(A-75,B-25)+servesoup(A-50,B-50)+servesoup(A-25,B-75))
                return memo[(A,B)]
        return n>4800 and 1 or servesoup(n,n)
