from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0]!='-':expression='+'+expression
        pre=''
        queue=[]
        for c in expression:
            if c in '-+':
                if pre:
                    queue.append(pre)
                    pre=c
                else:
                    pre=c
            else:
                pre+=c
        queue.append(pre)
        sm=Fraction('0/1')
        for n in queue:
            sm+=Fraction(n)
        sm=str(sm)
        if '/' not in sm:
            sm+='/1'
        return sm