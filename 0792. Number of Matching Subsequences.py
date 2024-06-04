class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res=0
        for word in words:
            cur=s
            for w in word:
                if w in cur:
                    p=cur.index(w)
                    cur=cur[p+1:]
                else:break
            else:res+=1
        return res
