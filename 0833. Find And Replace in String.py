class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        dic = {}
        for i, c in enumerate(s):
            dic[i] = c
        for p, i in enumerate(indices):
            cur = sources[p]
            for j in range(len(cur)):
                if i + j not in dic or s[i + j] != cur[j]:
                    break
            else:
                for n in range(i, i + len(cur)):
                    dic.pop(n)
                dic[i] = targets[p]
        pair = sorted(list(dic.items()))
        lst = [v for k, v in pair]
        return ''.join(lst)
