class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pre=1
        i=len(digits)-1
        while i>=0:
            if digits[i]<9:
                digits[i]+=pre
                pre=0
                break
            else:
                digits[i]=0
                i-=1
        if pre==1:
            digits=[1]+digits
        return digits
