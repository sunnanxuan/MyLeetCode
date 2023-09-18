class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = min([len(x) for x in strs])
        res = []
        for i in range(l):
            if all(s[i] == strs[0][i] for s in strs):
                res.append(strs[0][i])
            else:
                break
        return ''.join(res)
