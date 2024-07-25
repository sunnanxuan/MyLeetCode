class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordset=set(wordList)
        res=0
        used={beginWord}
        q=[beginWord]
        while q:
            res+=1
            new=[]
            for w in q:
                if w==endWord:return res
                for i in range(len(w)):
                    for c in string.ascii_lowercase:
                        cur=w[:i]+c+w[i+1:]
                        if cur in wordset and cur not in used:
                            new.append(cur)
                            used.add(cur)
            q=new
        return 0