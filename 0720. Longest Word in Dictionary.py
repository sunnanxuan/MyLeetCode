class Solution:
    def longestWord(self, words: List[str]) -> str:
        dic=collections.defaultdict(list)
        for w in words:
            bisect.insort(dic[w[:-1]+'*'],w)
        res=[0,'']
        def findword(s):
            if dic[s]:
                for c in dic[s]:
                    if len(c)>res[0]:
                        res[0]=len(c)
                        res[1]=c
                    findword(c+'*')
        findword('*')
        return res[1]