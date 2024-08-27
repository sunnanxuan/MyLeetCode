class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        lowers = {}
        for w in wordlist:
            if w.lower() not in lowers:
                lowers[w.lower()] = w

        wordset = set(wordlist)

        vowels = {}
        for word in wordlist:
            w = word.lower()
            cur = vowels
            for c in w:
                if c in 'aeiou': c = '*'
                if c in cur:
                    cur = cur[c]
                else:
                    cur[c] = {}
                    cur = cur[c]
            if '#' not in cur: cur['#'] = word

        res = []
        for q in queries:
            if q in wordset:
                res.append(q)
            elif q.lower() in lowers:
                res.append(lowers[q.lower()])
            else:
                cur = vowels
                for c in q.lower():
                    if c in 'aeiou': c = '*'
                    if c not in cur:
                        res.append('')
                        break
                    else:
                        cur = cur[c]
                else:
                    if '#' in cur:
                        res.append(cur['#'])
                    else:
                        res.append('')
        return res
