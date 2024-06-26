class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            l, r = s.split('@')

            res = l[0].lower() + '*' * 5 + l[-1].lower() + '@' + r.lower()
        else:
            lst = [c for c in s if c.isdigit()]
            if len(lst) == 10:
                res = '***-***-' + ''.join(lst[6:])
            else:
                res = '+' + '*' * (len(lst) - 10) + '-***-***-' + ''.join(lst[-4:])
        return res
