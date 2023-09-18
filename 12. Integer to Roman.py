class Solution:
    def intToRoman(self, num: int) -> str:
        def tansfer(n):
            if n >= 1000:
                return (n // 1000) * 'M' + tansfer(n % 1000)
            elif 1000 > n >= 900:
                return 'CM' + tansfer(n % 900)
            elif 900 > n >= 500:
                return 'D' + tansfer(n % 500)
            elif 500 > n >= 400:
                return 'CD' + tansfer(n % 400)
            elif 400 > n >= 100:
                return (n // 100) * 'C' + tansfer(n % 100)
            elif 100 > n >= 90:
                return 'XC' + tansfer(n % 90)
            elif 90 > n >= 50:
                return 'L' + tansfer(n % 50)
            elif 50 > n >= 40:
                return 'XL' + tansfer(n % 40)
            elif 40 > n >= 10:
                return (n // 10) * 'X' + tansfer(n % 10)
            elif n == 9:
                return 'IX'
            elif 9 > n >= 5:
                return 'V' + tansfer(n % 5)
            elif n == 4:
                return 'IV'
            elif 1 <= n <= 3:
                return 'I' * n
            elif n == 0:
                return ""

        res = tansfer(num)
        return res


