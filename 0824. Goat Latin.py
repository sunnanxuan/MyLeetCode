class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        lst = sentence.split()
        res = []
        c = 0
        for s in lst:
            c += 1
            if s[0] in 'aeiouAEIOU':
                res.append(s + 'ma' + 'a' * c)
            else:
                res.append(s[1:] + s[0] + 'ma' + 'a' * c)
        return ' '.join(res)
