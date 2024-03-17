class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        divisor={1}
        for i in range(2,int(num**0.5)+1):
            if not num%i:
                divisor.add(i)
                divisor.add(num//i)
        return num==sum(divisor)