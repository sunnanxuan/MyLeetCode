class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        rem = {}
        fraction = []
        if numerator * denominator >= 0:
            q = str(numerator // denominator)
        else:
            q = '-' + str(abs(numerator) // abs(denominator))
        r = abs(numerator) % abs(denominator)
        if r == 0:
            return q
        d = abs(denominator)
        i = 0
        r *= 10
        while r != 0 and r not in rem:
            fraction.append(str(r // d))
            nr = r % d
            rem[r] = i
            r = nr
            i += 1
            r *= 10
        if r == 0:
            res = q + '.' + ''.join(fraction)
        elif r in rem:
            j = rem[r]
            repaeting = fraction[j:]
            res = q + '.' + ''.join(fraction[:j]) + '(' + ''.join(fraction[j:]) + ')'
        return res

