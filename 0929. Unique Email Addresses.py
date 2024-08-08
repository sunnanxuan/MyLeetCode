class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dic = collections.defaultdict(set)
        for e in emails:
            l, d = e.split('@')
            l = l.replace('.', '')
            if '+' in l:
                ind = l.index('+')
                l = l[:ind]
            dic[d].add(l)
        res = sum([len(dic[k]) for k in dic])
        return res
