class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def divide(x, s):
            lx = len(x)
            ls = len(s)
            if ls % lx:
                return False
            else:
                if x * (ls // lx) == s:
                    return True
                else:
                    return False

        n = 1
        l1 = len(str1)
        l2 = len(str2)
        while n <= l1:
            if l1 % n:
                n += 1
            else:
                x = str1[:l1 // n]
                if divide(x, str1) and divide(x, str2):
                    return x
                else:
                    n += 1
        return ''
