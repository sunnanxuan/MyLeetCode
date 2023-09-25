class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(words[0])
        n = l * len(words)
        res = []
        dic_s = {}
        for i in range(len(s) - l + 1):
            if s[i:i + l] in words:
                dic_s[i] = s[i:i + l]
        dic_w = collections.Counter(words)
        for i in range(len(s) - n + 1):
            if i in dic_s:
                dic = collections.defaultdict(int)
                for j in range(i, i + n, l):
                    if j not in dic_s:
                        break
                    else:
                        dic[dic_s[j]] += 1
                if dic_w == dic:
                    res.append(i)
        return res

