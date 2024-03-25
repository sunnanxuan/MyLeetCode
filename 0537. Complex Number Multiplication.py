class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1=num1[:-1]
        num2=num2[:-1]
        r1,i1=num1.split('+')
        r2,i2=num2.split('+')
        r=int(r1)*int(r2)-int(i1)*int(i2)
        i=int(r1)*int(i2)+int(r2)*int(i1)
        return str(r)+'+'+str(i)+'i'