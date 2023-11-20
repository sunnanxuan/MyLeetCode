class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic=collections.defaultdict(list)
        for word in wordDict:
            dic[word[0]].append([word,len(word)])
        ind=[0]
        for i in ind:
            if i==len(s):
                return True
            if s[i] in dic:
                for w ,l in dic[s[i]]:
                    if w==s[i:i+l]:
                        if i+l not in ind:
                            ind.append(i+l)
        return False