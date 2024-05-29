class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        dic=collections.defaultdict(int)
        for c in licensePlate:
            if c.isalpha():dic[c.lower()]+=1
        words.sort(key=lambda x:(len(x)))
        for w in words:
            dic_w=collections.Counter(w)
            for k in dic:
                if k not in dic_w or dic[k]>dic_w[k]:
                    break
            else:return w