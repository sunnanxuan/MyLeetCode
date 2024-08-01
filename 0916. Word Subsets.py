class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        dic = collections.defaultdict(int)
        for w in words2:
            c = collections.Counter(w)
            for k in c:
                dic[k] = max(dic[k], c[k])
        res = []
        for w in words1:
            c = collections.Counter(w)
            for k in dic:
                if k not in c or dic[k] > c[k]:
                    break
            else:
                res.append(w)
        return res
