class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic=collections.defaultdict(list)
        for word in wordDict:
            dic[word[0]].append([word,len(word)])
        res=[]
        def segment(i,arr):
            if i>=len(s):
                if arr:
                    res.append(' '.join(arr))
                    arr.pop()
            elif s[i] not in dic:
                if arr:arr.pop()
            else:
                for w,l in dic[s[i]]:
                    if w==s[i:i+l]:
                        segment(i+l,arr+[w])
        segment(0,[])
        return res
