class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for w in words:
            dic_w = {}
            dic_p = {}
            for i, p in enumerate(pattern):
                if w[i] not in dic_w and p not in dic_p:
                    dic_p[p] = w[i]
                    dic_w[w[i]] = p
                elif w[i] not in dic_w or p not in dic_p or dic_p[p] != w[i] or dic_w[w[i]] != p:
                    break
            else:
                res.append(w)
        return res
