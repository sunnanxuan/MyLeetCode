class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ind, res = {w:i for i, w in enumerate(words)}, []
        for i,w in enumerate(words):
            l=len(w)
            for j in range(l+1):
                pre=w[:j]
                suf=w[j:]
                if pre[::-1]==pre:
                    suf=suf[::-1]
                    if suf!=w and suf in ind:
                        res.append([ind[suf],i])
                if j!=l and suf[::-1]==suf:
                    pre=pre[::-1]
                    if pre!=w and pre in ind:
                        res.append([i,ind[pre]])
        return res
