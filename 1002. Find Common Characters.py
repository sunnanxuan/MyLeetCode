class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic=collections.Counter(words[0])
        for w in words[1:]:
            w_dic=collections.Counter(w)
            for k in dic:
                dic[k]=min(dic[k],w_dic.get(k,0))
        res=[]
        for k in dic:
            res.extend([k]*dic[k])
        return res