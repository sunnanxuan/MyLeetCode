class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ban = set()
        inds = collections.defaultdict(list)
        for i, c in enumerate(senate):
            inds[c].append(i)
        r = list(inds['R'])
        d = list(inds['D'])
        i = 0
        while r and d:
            if senate[i] == 'R':
                p = bisect.bisect(d, i)
                if p == len(d):ban.add(d.pop(0))
                else:ban.add(d.pop(p))
            elif senate[i] == 'D':
                p = bisect.bisect(r, i)
                if p == len(r):ban.add(r.pop(0))
                else:ban.add(r.pop(p))
            i += 1
            if i == len(senate): i = 0
            while i in ban:
                i += 1
                if i == len(senate): i = 0
        if r:return 'Radiant'
        else:return 'Dire'
