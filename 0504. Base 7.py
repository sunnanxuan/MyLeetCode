class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        res = []
        p = ''
        if num < 0:
            p = '-'
        num = abs(num)
        while num > 0:
            res.append(str(num % 7))
            num //= 7
        return p + ''.join(res[::-1])
